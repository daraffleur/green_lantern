from django.contrib import admin

# Register your models here.
from apps.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image',)
