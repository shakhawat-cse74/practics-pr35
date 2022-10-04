from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_name(self):
        val=self.cleaned_data['name']
        if len(val)< 5:
         raise forms.ValidationError('Enter more than 5 charecter')
        return val
    
    def clean_password(self):
        pa=self.cleaned_data['password']
        if len(pa)< 8:
         raise forms.ValidationError('Enter more than 8 and Specia Charecter')
        return pa