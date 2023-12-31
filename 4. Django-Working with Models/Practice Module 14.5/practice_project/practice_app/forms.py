from django import forms
import datetime

class Practice_Form(forms.Form):
    name = forms.CharField(max_length = 30, initial='Mahadi Hasan Munna')

    # comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))

    email = forms.EmailField(required = False, label="Please enter your email address",)

    agree = forms.BooleanField(initial=True)

    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),initial=datetime.date.today)

    BIRTH_YEAR_CHOICES=[1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006]
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    value = forms.DecimalField()

    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    # favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)

    roll_number = forms.IntegerField(  
                     help_text = "Enter 6 digit roll number"
                     )  
