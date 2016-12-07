# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.admin.helpers import ActionForm
from django.contrib.auth.forms import UserChangeForm, AdminPasswordChangeForm
from django.utils.translation import ugettext_lazy as _
from crwyadmin.models import CrwyadminConfig


class CrwyActionForm(ActionForm):
    action = forms.ChoiceField(label=_('Action:'), widget=forms.Select(attrs={'class': 'form-control', 'id': 'action'}))


class CrwyUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CrwyUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control'})
        self.fields['groups'].widget = forms.SelectMultiple(attrs={'class': 'form-control'})
        self.fields['user_permissions'].widget = forms.SelectMultiple(attrs={'class': 'form-control'})
        self.fields['last_login'].widget = forms.DateTimeInput(attrs={'class': 'form-control'})
        self.fields['date_joined'].widget = forms.DateTimeInput(attrs={'class': 'form-control'})


class CrwyAdminPasswordChangeForm(AdminPasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CrwyAdminPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})


class CrwyConfigForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CrwyConfigForm, self).__init__(*args, **kwargs)
        self.fields['is_register'].widget = forms.CheckboxInput()
        self.fields['is_forgetpasswd'].widget = forms.CheckboxInput()
        self.fields['manager_email'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['version'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['version'].disabled = True
        self.fields['version'].required = True

    class Meta:
        model = CrwyadminConfig
        exclude = ('slug',)


class LoginForm(forms.Form):
    """不直接继承model类，以避免username做唯一性检查"""
    username = forms.CharField(required=True, error_messages={'required': "用户名不能为空"})
    password = forms.CharField(required=True, min_length=6, max_length=10, error_messages={'required': "密码不能为空", 'min_length': "密码最小长度为六位", 'max_length': '密码最大长度为十位'})


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['password'].required = True
        self.fields['password'].min_length = 6
        self.fields['password'].max_length = 10
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        error_messages = {
            'username': {'required': "用户名不能为空", 'invalid': "不是一个有效的用户名格式"},
            'password': {'required': "密码不能为空", 'min_length': "密码最小长度为六位", 'max_length': '密码最大长度为十位'},
            'email': {'required': "邮箱不能为空", 'invalid': "不是一个有效的邮箱格式"}
        }
