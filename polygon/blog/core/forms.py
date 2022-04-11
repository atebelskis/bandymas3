from django import forms
from .models import Nariai

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Nariai
        fields = '__all__'