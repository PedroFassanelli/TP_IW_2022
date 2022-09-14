from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from sitio.models import Publicacion, Comentario

class FormNuevaPublicacion(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ('title','text', 'location', 'is_public', 'image_one', 'image_two', 'image_three')
    
    def __init__(self, *args, **kwargs):
        super(FormNuevaPublicacion, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = "Titulo"

        self.fields['text'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['placeholder'] = "Texto"

class FormNuevoComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('text', )
    
    def __init__(self, *args, **kwargs):
        super(FormNuevoComentario, self).__init__(*args, **kwargs)

        self.fields['text'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['placeholder'] = "Texto"