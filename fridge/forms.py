from django import forms
from .models import Post, Copost
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'family', 'date', 'month', 'year', 'img', )

        labels = {
            'name':'이름',
            'family':'카테고리',
            'date':'구매일',
            'month':'',
            'year':'',
            'img':'사진업로드'
        }

        widgets = {
            'name':forms.TextInput(attrs={
                'placeholder':' 무엇을 사셨나요?',
                'size':'20'
            })
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder':'Username', 'size':'20'}),
            'username': forms.TextInput(attrs={'placeholder':'Password', 'size':'20'})
            }
        help_texts = {
            'username': None,
        }



class CopostForm(forms.ModelForm):
    class Meta:
        model = Copost
        fields = ('title', 'user_name', 'contents',)