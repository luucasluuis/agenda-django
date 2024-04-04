from django.contrib import admin
from contact.models import Contact


# é necessario registrar o model
# configuração do model na admin do django
# uma das formas é com o decorator @admin do django

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = '-id',  # id decrescente
    # list_filter = 'created_data', 
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name',
    list_display_links = 'id', 'phone',
    