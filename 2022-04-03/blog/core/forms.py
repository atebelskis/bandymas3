from django import forms
from django.forms import ModelForm, CharField, EmailField
from .models import Post
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']          #kol kas email nereikaluaism/nedarysim



class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostUpdateForm(ModelForm):
    name = CharField(label='Post Name', required=True, help_text="Please enter your post name")   #formoje galima pakisti laukeliu pavad ir kt. par
    #email = EmailField(label='Email', required=True, help_text="Please enter your email")

    class Meta:
        model = Post
        fields = '__all__'

    def clean(self):               #ant 'name' uzdeda apribojima tamtikram skaiciui charakteriu
        super(PostUpdateForm, self).clean()
        name = self.cleaned_data.get('name')
        address = self.cleaned_data.get('address')
        if len(name) <5:
            self.errors['name'] = self.error_class(["minimum 5 char reuquired"])
        elif len(address) <10:
            self.errors['address'] = self.error_class(["minimum 10 char reuquired"])
        return self.cleaned_data
'''
    def clean_address(self):
        super(PostUpdateForm, self).clean()
        address = self.cleaned_data.get('address')
        if len(address) <10:
            self.errors['address'] = self.error_class(["minimum 10 char reuquired"])
        return self.cleaned_data
'''