import django_tables2 as tables
from .models import FXTaskSpec



class FXTaskSpecTable(tables.Table):
    rowsel = tables.CheckBoxColumn(verbose_name='Select', accessor='pk')

    class Meta:
        model = FXTaskSpec
        template_name = "bulma-table.html"


    def __init__(self, *args, **kwargs):
        super(FXTaskSpecTable, self).__init__(*args, **kwargs)
        self.columns['rowsel'].column.verbose_name = 'Select'
        self.columns['raised_date'].column.verbose_name = 'Date'
