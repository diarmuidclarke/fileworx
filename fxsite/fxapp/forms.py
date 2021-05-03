import datetime
from django import forms
from django.core.cache import cache
from django.db.models.fields import FilePathField
from django.forms import fields
from django.forms.widgets import CheckboxInput, RadioSelect
from django.contrib.auth.models import User as authUser
from django.core.cache import cache
from .utils_file import get_files
from .models import FXSource, FXTaskSpec




class FXSubmitDocStage2(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'


    
    date = cache.get('dit:stage1:date')
    user = cache.get('dit:stage1:user')
    src = cache.get('dit:stage1:src')

    qs_path_src = FXSource.objects.filter(source_path_friendlyname = src)
    if len(qs_path_src) >= 1:
        path_src = qs_path_src[0].source_path
        list_files = get_files(path_src, ['.docx', '.doc'])

        list_file_choices = []
        for i,f in enumerate(list_files):
            tup = (str(i),f )
            list_file_choices.append(tup)        
    else:
        list_file_choices = []

    file_choice= forms.ChoiceField( choices = list_file_choices, required=True, widget=CheckboxInput ) 
    





class FXSubmitDocStage1(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    
    raised_date = forms.DateField(initial=datetime.datetime.now(),required=True)
    raised_date.disabled = True

    raised_by = forms.CharField(max_length=10, initial = 'fred3' , required= True)
    raised_by.disabled = True

    # list of sources to select
    qs_sources = FXSource.objects.all()
    list_tup = []
    for src in qs_sources:
        tup = ( src.source_path_friendlyname , src.source_path )
        list_tup.append(tup)
    choice_source = forms.ChoiceField(choices = list_tup)





class FXSubmitTaskForm(forms.ModelForm):

    # file_source_doc_path = forms.ModelChoiceField(
    #     queryset=FXSource.objects.all(),
    #     widget=Select2Widget(
    #        attrs={ "data-width" : "20em"}
    #     )
    # )

    # doc_selector = forms.ModelChoiceField(
    #     queryset = None, # FXSource.objects.all()
    #     search_fields=['name_icontains'],
    #     widget = ModelSelect2Widget(
    #         attrs={ "data-width" : "20em", 'data-minimum-input-length' : 0, }
    #     ),
    #     dependent_fields=['file_source_doc_path']
    # )

    class Meta:
        model = FXTaskSpec
        fields = '__all__'
        widgets = {
            'dest': RadioSelect(),  # attrs={'cols': 80, 'rows': 20}
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


    def clean_raised_by_userac(self):
        return self.cleaned_data['raised_by_userac']
