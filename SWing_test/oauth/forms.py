from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from .models import User, UserManager

class UserCreationForm(forms.ModelForm):
    
    student_id=forms.IntegerField(
        label=_('Student_id'),
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Student_id'),
                'required': 'True',
            }
        )
    )
    
    email=forms.EmailField(
        label=_('Email Address'),
        required=True,
        widget=forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': _('Email_Address'),
                'required': 'True',
            }
        )
    )
    
    username=forms.CharField(
        label=_('Name'),
        required=True,
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': _('Student_Name'),
                'required': 'True',
            }
        )
    )
    class Meta:
        model = User
        fields = ('student_id', 'email', 'username')
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.student_id = self.cleaned_data['student_id']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('student_id', 'email', 'username', 'password', 'is_active', 'is_superuser', 'is_admin', 'is_staff')
