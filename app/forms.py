from django import forms
from django.core import validators
def name_valid(a):                                               # 1)Normal Function 
    if a[0]=='z' or len(a)<5:
        raise forms.ValidationError('Please enter valid name')
        

class NameForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[name_valid])
    age=forms.IntegerField()
    email=forms.EmailField(validators=[validators.RegexValidator('[a-zA-z1-9]\w*[.]?\w+@gmail[.]com')])
    remail=forms.EmailField()
    mobile = forms.CharField(max_length=10, min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    bot = forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)  # Bot catcher element

    def clean(self):                                                  # 2)classmethod - clean- method to validate more than one input element
        e=self.cleaned_data['email']
        r=self.cleaned_data['remail']

        if e!=r :
            raise forms.ValidationError('Please renter the email')

    #def clean_age(self):                                             # classmethod - cleanelement - method to validate one input element
    #       if self.cleaned_data['age'] <18:
     #       raise forms.ValidationError('You are under age')

    def clean_bot(self):                                             # 3)classmethod - cleanelement - method to validate one input element
        if len(self.cleaned_data['bot']) >0:
            raise forms.ValidationError('You caught into trap')      # clean_element method is only used bot catching