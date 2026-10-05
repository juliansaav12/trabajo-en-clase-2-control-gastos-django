from django.contrib import admin
from .models import Gasto

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'monto', 'categoria', 'fecha', 'pagado', 'usuario')
    list_filter = ('categoria', 'pagado')
    search_fields = ('descripcion',)