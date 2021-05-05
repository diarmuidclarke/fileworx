import django_tables2 as tables
from .models import FXTaskSpec



class FXTaskSpecTable(tables.Table):
    class Meta:
        model = FXTaskSpec
        template_name = "bulma-table.html"


