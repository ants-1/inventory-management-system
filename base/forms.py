from django import forms
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