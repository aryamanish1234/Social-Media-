from django import forms
from .models import Profile

class ProfileModeForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ('first_name', 'last_name', 'bio','avatar')