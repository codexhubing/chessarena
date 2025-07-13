from django import forms
from allauth.account.forms import SignupForm
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        Profile.objects.create(user=user)
        return user