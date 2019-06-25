from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=10, min_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'email',
            'phone',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']

        if commit:
            user.save()

        return user

class LoginForm(AuthenticationForm):
    CHOICES=[('buyer','As a Buyer'),
         ('seller','As a Seller')]

    login_as = forms.ChoiceField(label="How do you want to Login?",choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'login_as',
        )
    
    def save(self, commit=True):
        user.login_as = self.cleaned_data['login_as']

        if commit:
            user.save()

        return user
     
