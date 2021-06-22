from django.contrib import admin
from app.api.models import News

# Register your models here.

# Cambia el nombre que ve el usuario en el panel de adminsitración
admin.site.site_header = "Admin de mi HakerNews"

# Opcion personalizable de importación de  tablas
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # Campos de solo lectura
    readonly_fields = ('votes',)
    # Ver los campos en la vista
    list_display = ('title', 'votes')
