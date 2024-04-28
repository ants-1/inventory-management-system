from django import forms
from .models import *


class AddEquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = [
            "name",
            "type",
            "description",
            "quantity",
            "borrow_date",
            "return_date",
            "audit_date",
            "status",
            "serial_number",
            "comments",
            "location",
            "img_url",
        ]
        
class EditEquipmentForm(forms.ModelForm):    
    class Meta:
        model = Equipment
        fields = [
            "name",
            "type",
            "description",
            "quantity",
            "borrow_date",
            "return_date",
            "audit_date",
            "status",
            "serial_number",
            "comments",
            "location",
            "img_url",
        ]