from django import forms
from .models import User
from .models import Post
from .models import RegexValidator

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['first_name','last_name','username','email','bio']
        widgets = {'bio' : forms.Textarea()}
    new_password= forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        validators=[RegexValidator(regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*s',
        message='Password must contain an upppercase character, a lowercase character and a numebr')]
    )
    password_confirmation= forms.CharField(label='Password confirmation', widget=forms.PasswordInput())

def clean(self):
    super().clean()
    new_password=self.cleaned_data.get('new_password')
    password_confirmation=self.cleaned_data.get('password_confirmation')
    if new_password !=password_confirmation:
        self.add_error('password_confirmation','confirmation does not match')

def save(self):
    super().save(commit=False)
    user=User.objects.create_user(
        self.cleaned_data.get("username"),
        first_name=self.cleaned_data.get("first_name"),
        last_name=self.cleaned_data.get("last_name"),
        email=self.cleaned_data.get("email"),
        bio=self.cleaned_data.get("bio"),
        password=self.cleaned_data.get("new_password"),

    )
    return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['text']
        widgets = {'text' : forms.Textarea()}
