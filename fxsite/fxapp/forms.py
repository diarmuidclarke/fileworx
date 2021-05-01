from django import forms
from django.forms import fields
from .models import FXTaskSpec


class FXSubmitTaskForm(forms.ModelForm):
    # uploadfile = forms.FileField(label='my file to upload!')

    class Meta:
        model = FXTaskSpec
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        super(FXSubmitTaskForm, self).__init__(*args, **kwargs)
