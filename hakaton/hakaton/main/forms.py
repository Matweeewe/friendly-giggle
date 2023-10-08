from .models import Tiket
from django.forms import ModelForm, TextInput, Textarea

class TiketForm (ModelForm):
    class Meta:
        model = Tiket
        fields = ["title", "tiket"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название тикета'
            }),
            "tiket": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите свою проблему'
            }),
        }