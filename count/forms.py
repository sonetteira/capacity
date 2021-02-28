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