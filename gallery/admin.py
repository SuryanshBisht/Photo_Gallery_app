from django.contrib import admin
from gallery.models import Photo, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)