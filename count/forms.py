from django import forms
from .models import *

class OrgForm(forms.ModelForm):
    class Meta:
        model = Org
        fields = '__all__'

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class AdminUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fname','lname','password','admin','active']
        widgets = {
            'password': forms.PasswordInput(),
            'admin': forms.HiddenInput(attrs={'value':'1'}),
            'active': forms.HiddenInput(attrs={'value':'1'}),
        }