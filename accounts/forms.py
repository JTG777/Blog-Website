from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['date_of_birth','bio','profile_picture']
        labels={'date_of_birth':'Date of birth','bio':'Bio','profile_picture':'Profile Picture'}
        widgets={'date_of_birth':forms.DateInput(attrs={'type':'date'})}




