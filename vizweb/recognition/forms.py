from django import forms
from recognition.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("image",)
