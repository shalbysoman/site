from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['image', 'title', 'date', 'category', 'actors', 'description', 'trailer', 'username']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'actors': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'trailer': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Enter movie Name:',
            'image': 'Select an Image: ',
            'date': 'Enter Release Date:',
            'category': 'Select Category: ',
            'actors': 'Enter actors: ',
            'description': 'Enter a Description: ',
            'trailer': 'Enter trailer link:',
            'username': 'Enter your username:',

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }



