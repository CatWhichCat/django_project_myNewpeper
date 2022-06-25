from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']
        
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название статьи',
                }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата и время'
            }),
            "full_text": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Текс статьи'
            })
        }