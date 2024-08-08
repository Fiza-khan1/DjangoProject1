from django import forms
from .models import UploadedFile
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class ModelFormWithFileField(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['title', 'file']
