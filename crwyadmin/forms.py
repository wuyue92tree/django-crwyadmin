# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User, Group
from .models import *


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


# class AccountsColumnsForm(forms.ModelForm):
#     class Meta:
#         model = AccountsColumns
#         fields = ('level', 'name', 'link', 'link_type', 'is_link', 'icon', 'parent_id', 'tag', 'app')


class AccountsUsersForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AccountsUsersForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'groups', 'is_active', 'is_staff', 'is_superuser')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '邮箱'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '姓'}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-control'}),
            # 'is_active': forms.Checkbox(attrs={'class': 'form-control'}),
            # 'is_staff': forms.CheckboxInput(attrs={'class': 'form-control'}),
            # 'is_superuser': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

class AccountsGroupsForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用户组名称'}),
            'permissions': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }