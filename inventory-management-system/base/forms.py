from typing import Any
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from .models import *

class AddEquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = "__all__"

class EditEquipmentForm(forms.ModelForm):    
    class Meta:
        model = Equipment
        fields = "__all__"

class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
