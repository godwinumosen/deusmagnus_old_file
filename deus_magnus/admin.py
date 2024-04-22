from django.contrib import admin
# Register your models here.
from . import models
from .models import DeusMagnusMainPost, SecondDeusMagnusMainPicturePost, LastDeusMagnusMainPicturePost

#The DeusMagnus post post model admin of josepdam
class DeusMagnusMainPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'deus_magnus_slug': ('deus_magnus_title',)}
    list_display = ['deus_magnus_title','deus_magnus_description','deus_manus_video','deus_magnus_author']
admin.site.register(DeusMagnusMainPost, DeusMagnusMainPostModelAdmin)

#The Secon DeusMagnus post post model admin of josepdam
class SecondDeusMagnusMainPicturePosttModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'second_deus_magnus_slug': ('second_deus_magnus_title',)}
    list_display = ['second_deus_magnus_title','second_deus_magnus_description','second_deus_magnus_img','second_deus_magnus_author']
admin.site.register(SecondDeusMagnusMainPicturePost, SecondDeusMagnusMainPicturePosttModelAdmin)

#The last sub category of the home page view
class LastDeusMagnusMainPicturePostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'last_deus_magnus_slug': ('last_deus_magnus_title',)}
    list_display = ['last_deus_magnus_title','last_deus_magnus_description','last_deus_magnus_image','last_deus_magnus_author']
admin.site.register(LastDeusMagnusMainPicturePost, LastDeusMagnusMainPicturePostModelAdmin)