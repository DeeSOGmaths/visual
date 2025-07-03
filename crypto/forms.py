from django import forms

#creating my forms

class RegistrationForm(forms.Form):
    FirstName = forms.CharField(max_length = 250)
    LastName = forms.CharField(max_length = 250)
    email = forms.EmailField(max_length = 100)
    password = forms.CharField(max_length = 100)



class LoginForm(forms.Form):
    email = forms.EmailField(max_length = 100)
    password = forms.CharField(max_length = 100)
    users_share = forms.ImageField()