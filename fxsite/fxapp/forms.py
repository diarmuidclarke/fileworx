from django import forms
from django.db.models.fields import FilePathField
from django.forms import fields
from django.forms.widgets import RadioSelect
from .models import FXSource, FXTaskSpec
from django.contrib.auth.models import User as authUser
import datetime




class FXSubmitTaskForm(forms.ModelForm):
   

    class Meta:
        model = FXTaskSpec
        fields =  '__all__'
        widgets = {
            'dest': RadioSelect(), #attrs={'cols': 80, 'rows': 20}
        }


    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})

        dt = datetime.datetime.now()
        dts = dt.strftime('%d/%m/%Y')
        initial['raised_date'] = dts

        initial['raised_by_userac'] = kwargs.pop('user', None)

        super(FXSubmitTaskForm, self).__init__(*args, **kwargs)

        self.fields['raised_date'].disabled = True
        self.fields['raised_by_userac'].disabled = True
