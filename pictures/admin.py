from django.contrib import admin
from .models import Editor,Location,Category,Image

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('Location',)

# Register your models here.
admin.site.register(Editor)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image)



