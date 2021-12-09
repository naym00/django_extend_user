from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators


def name_error(name):
    error = True
    for i in name:
        if "A" <= i <= "Z" or "a" <= i <= "z" or i == "." or i == " ":
            error = False
        else:
            error = True
            break
    if error:
        raise forms.ValidationError("Invalid Name!")


def phone_number_error(ph_n):
    error = True
    if len(ph_n) == 14:
        if ph_n[0] == '+' and ph_n[1] == '8' and ph_n[2] == '8' and ph_n[3] == '0' and ph_n[4] == '1' and (
                '3' <= ph_n[5] <= '9'):
            for i in range(6, len(ph_n), 1):
                if '0' <= ph_n[i] <= '9':
                    error = False
                else:
                    error = True
                    break
    elif len(ph_n) == 11:
        if ph_n[0] == '0' and ph_n[1] == '1' and ('3' <= ph_n[2] <= '9'):
            for i in range(3, len(ph_n), 1):
                if '0' <= ph_n[i] <= '9':
                    error = False
                else:
                    error = True
                    break
    if error:
        raise forms.ValidationError("Invalid Phone Number!")


def gender_error(gender):
    gender = gender.capitalize()
    if gender == "Male" or gender == "Female" or gender == "Trans gender":
        pass
    else:
        raise forms.ValidationError("Invalid Gender! Example: Male, Female, Trans gender")


def username_error(username):
    error = True
    for i in username:
        if "a" <= i <= "z" or "0" <= i <= "9" or i == "@" or i == "." or i == "+" or i == "-" or i == "_":
            error = False
        else:
            error = True
            break
    if error:
        raise forms.ValidationError("Invalid Username! Lower letters, digits and @/./+/-/_ only.")


class UserForm(UserCreationForm):
    # This Field has come from UserCreationForm.
    # Customizing it here according to our wish
    first_name = forms.CharField(validators=[validators.MinLengthValidator(3),
                                             validators.MaxLengthValidator(50),
                                             name_error], required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}), label='')
    # This Field has come from UserCreationForm.
    # Customizing it here according to our wish
    last_name = forms.CharField(validators=[validators.MinLengthValidator(3),
                                            validators.MaxLengthValidator(50),
                                            name_error], required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), label='')
    # This Field has come from UserCreationForm.
    # Customizing it here according to our wish
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'example@gmail.com'}),
                             label='')
    phone_number = forms.CharField(validators=[validators.MinLengthValidator(11),
                                               validators.MaxLengthValidator(14),
                                               phone_number_error], required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}), label='')
    gender = forms.CharField(validators=[validators.MinLengthValidator(4),
                                         validators.MaxLengthValidator(12),
                                         gender_error], required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Male/Female/Trans gender'}), label='')
    # This Field has come from UserCreationForm.
    # Customizing it here according to our wish
    username = forms.CharField(validators=[validators.MinLengthValidator(5),
                                           validators.MaxLengthValidator(150),
                                           username_error], required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}), label='')
    # This Field has come from UserCreationForm.
    # Customizing it here according to our wish
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')
    # This Field has come from UserCreationForm.
    # Customizing it here according to our wish
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), label='')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'gender', 'username', 'password1', 'password2')
