from django import forms
from .models import Transaction
from accounts.models import UserBankAccount
from .constants import BANKRUPT

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
            'transaction_type'
        ]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account') # account value ke pop kore anlam
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True # ei field disable thakbe
        self.fields['transaction_type'].widget = forms.HiddenInput() # user er theke hide kora thakbe

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()


class DepositForm(TransactionForm):
    def clean_amount(self): # amount field ke filter korbo
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount') # user er fill up kora form theke amra amount field er value ke niye aslam, 50
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )

        return amount


class WithdrawForm(TransactionForm):

    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance # 1000
        amount = self.cleaned_data.get('amount')
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount} $'
            )

        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at most {max_withdraw_amount} $'
            )

        if amount > balance: # amount = 5000, tar balance ache 200
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not withdraw more than your account balance'
            )
        if BANKRUPT:
            raise forms.ValidationError(
                f'You can not withdraw at this momment. The bank is bankrupt!'
            )
        return amount



class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        return amount
    
class TransferForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
            'transaction_type',
            'receiver_account_no'
        ]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account') # account value ke pop kore anlam
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True # ei field disable thakbe
        self.fields['transaction_type'].widget = forms.HiddenInput() # user er theke hide kora thakbe

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()

class SendMoneyForm(TransferForm):

    def clean_amount(self):
        account = self.account
        min_transfer_amount = 100
        max_transfer_amount = 10000
        balance = account.balance
        amount = self.cleaned_data.get('amount')
        if amount < min_transfer_amount:
            raise forms.ValidationError(
                f'You can transfer at least {min_transfer_amount} $'
            )

        if amount > max_transfer_amount:
            raise forms.ValidationError(
                f'You can transfer at most {max_transfer_amount} $'
            )

        if amount > balance:
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not transfer more than your account balance'
            )

        return amount
    def clean_receiver_account_no(self):
        receiver_acc = self.cleaned_data.get('receiver_account_no')
        try:
            receiver = UserBankAccount.objects.get(account_no=receiver_acc)
        except:
            raise forms.ValidationError(
                f'No user found with account no {receiver_acc}'
            )
        return receiver_acc