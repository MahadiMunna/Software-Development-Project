from django import forms
from model_form_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        # fields = ['name','roll']
        # exclude = ['roll']
        fields = '__all__'
        labels = {
            'name':'Enter Student Name',
            'roll':'Enter Student Roll'
        }
        # widgets = {
        #     'name':forms.PasswordInput()
        # }
        help_texts = {
            'name':'Write your full name'
        }
        error_messages = {
            'name': {'required':'Your name is required'}
        }