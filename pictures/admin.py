from django.contrib import admin
from .models import Editor,Location,Category,Image

# Register your models here.
# class ImageAdmin(admin.ModelAdmin):
#     filter_horizontal =['image_category',]
# 'bootstrap3''bootstrap3'
admin.site.register(Editor)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image)



