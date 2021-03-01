from django import forms
from .models import *

class OrgForm(forms.ModelForm):
    class Meta:
        model = Org
        fields = '__all__'

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name','org','max_capacity']
        widgets = {
            'org': forms.HiddenInput(),
        }

class AdminUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fname','lname','uname','password','admin','active']
        widgets = {
            'password': forms.PasswordInput(),
            'admin': forms.HiddenInput(attrs={'value':'1'}),
            'active': forms.HiddenInput(attrs={'value':'1'}),
        }

class LoginForm(forms.Form):
    uname = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=1024, widget=forms.PasswordInput())

    def clean(self):
        try:
            user = User.objects.get(uname=self.cleaned_data.get('uname'), password=self.cleaned_data.get('password'))
        except User.DoesNotExist:
            raise forms.ValidationError("Incorrect username or password.")
        return super().clean()