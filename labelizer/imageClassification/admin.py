from django.contrib import admin
from .models import Image, Classe

admin.site.register(Classe)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'classe')
    list_filter = ('classe',)
    search_fields = ('image',)

# @admin.register(Classe)
# class ClasseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'nom', 'image')
