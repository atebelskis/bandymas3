from django import forms
from .models import Member

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'