from django import forms
from django.core import validators

# Django built in form 
# widgets = field to html input
class ContactForm(forms.Form):
    name = forms.CharField(label="Full Name: ", help_text="Enter your full name", required=False, disabled=True, widget = forms.Textarea(attrs={'class': 'form-control', 'id':'text-area', 'placeholder':'Enter your full name'}))
    # file = forms.FileField()
    # email = forms.EmailField(label="User Email")
    # age = forms.IntegerField(label="Enter age", widget= forms.NumberInput)
    # weight = forms.FloatField(label="Enter weight")
    # Balance = forms.DecimalField(label="Enter Balance")
    # check = forms.BooleanField(label="Accept")
    # birthday = forms.DateField(label="Enter Birth Day", widget= forms.DateInput(attrs={'type':'date'}))
    appointment = forms.CharField(label="Enter Appointment", widget=forms.DateInput({'type':'datetime-local'}))
    CHOICES = [('S','Small'),('M','Medium'),('L','Long')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    meal = [('p','Pepperoni'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=meal, widget=forms.CheckboxSelectMultiple)

# validation using user define function 
# class StudentForm(forms.Form):
#     name = forms.CharField(label='Enter name')
#     email = forms.CharField(label='Enter email')
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Enter valid email")
    #     return valemail

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Enter valid email")


# validation using built-in validator
def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter at lest 10 characters")
         
class StudentForm(forms.Form):

    name = forms.CharField(label='Enter name', widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='Enter a name with at least 10 characters')])
    text = forms.CharField(label='Enter text', widget=forms.TextInput, validators=[len_check])
    email = forms.CharField(label='Enter email', widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter valid email')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message='Age must be less than 34'), validators.MinValueValidator(24, message='Age must be greater than 24')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['png'], message='File must be png')])


class PasswordValidator(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    repass = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        valpass = self.cleaned_data['password']
        valrepass = self.cleaned_data['repass']
        if valpass != valrepass:
            raise forms.ValidationError("Password doesn't match")