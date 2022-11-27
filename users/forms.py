from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class SignupForm(forms.Form):
    username = forms.CharField(max_length=120,
                                widget=forms.TextInput
                                (attrs={'class': 'my_input',
                                        }))
    email = forms.CharField(max_length=100,
                            widget=forms.EmailInput
                            (attrs={'class': 'my_input',
                                   }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'my_input',}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'my_input',}))

    def clean(self):
        cd = self.cleaned_data

        password1 = cd.get("password1")
        password2 = cd.get("password2")

        if password1 != password2:
            # Or you might want to tie this validation to the password1 field
            raise forms.ValidationError("Passwords did not match")


