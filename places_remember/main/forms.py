from .models import Post
from django.forms import ModelForm, TextInput, Textarea


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ["title", "description", "latitude", "longitude"]
        widgets = {
            "title": TextInput(attrs={
                "id": "title",
                "class": "form-control",
                "placeholder": "Название",
            }),
            "description": Textarea(attrs={
                "id": "description",
                "class": "form-control",
                "placeholder": "Описание",
            }),
            "latitude": TextInput(attrs={
                "id": "latitude",
                "class": "form-control",
                "placeholder": "Широта",
                "readonly": "readonly"
            }),
            "longitude": TextInput(attrs={
                "id": "longitude",
                "class": "form-control",
                "placeholder": "Долгота",
                "readonly": "readonly"
            }),
        }
