from django.contrib import admin
from .models import Avto
from django.utils.html import format_html
# admin.site.register(MediaUser)

@admin.register(Avto)
class AvtoAdim(admin.ModelAdmin):
    def rename_blog_title(self, obj):
        return obj.text[:150]
    rename_blog_title.short_description = 'text'


