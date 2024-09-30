from django.contrib import admin
# Register your models here.
from . import models
from .models import DeusMagnusMainPost, SecondDeusMagnusMainPicturePost, LastDeusMagnusMainPicturePost,SubPicture_2
from .models import SubPicture_1, VideoSubImage, DeusMagnusEventBlog,OurManagementsInDeusMagnus,FAQs
from .models import GLOSSARY,Mainvideo,BlogDeusMagnus,Guides,Contactvideo
#The DeusMagnus post,post model admin


class MainvideoModelAdmin (admin.ModelAdmin):
    list_display = ['deus_magnus_first_video']
admin.site.register(Mainvideo, MainvideoModelAdmin)

class ContactvideoModelAdmin (admin.ModelAdmin):
    list_display = ['deus_magnus_contact_video']
admin.site.register(Contactvideo, ContactvideoModelAdmin)
#The DeusMagnus main post model admin
class DeusMagnusMainPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'deus_magnus_slug': ('deus_magnus_title',)}
    list_display = ['deus_magnus_title','deus_magnus_description','deus_manus_video','deus_magnus_author']
admin.site.register(DeusMagnusMainPost, DeusMagnusMainPostModelAdmin)

#The Second DeusMagnus post post model admin of josepdam
class SecondDeusMagnusMainPicturePosttModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'second_deus_magnus_slug': ('second_deus_magnus_title',)}
    list_display = ['second_deus_magnus_title','second_deus_magnus_description','second_deus_magnus_img','second_deus_magnus_author']
admin.site.register(SecondDeusMagnusMainPicturePost, SecondDeusMagnusMainPicturePosttModelAdmin)

#The last sub category of the home page view
class LastDeusMagnusMainPicturePostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'last_deus_magnus_slug': ('last_deus_magnus_title',)}
    list_display = ['last_deus_magnus_title','last_deus_magnus_description','last_deus_magnus_image','last_deus_magnus_author']
admin.site.register(LastDeusMagnusMainPicturePost, LastDeusMagnusMainPicturePostModelAdmin)

#The inner sub category of the detailview page view
class SubPicture_1_ModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'sub_slug_1': ('sub_title_1',)}
    list_display = ['sub_title_1','sub_description_1','sub_image_1','sub_author_1']
admin.site.register(SubPicture_1, SubPicture_1_ModelAdmin)

#The inner second sub category of the detailview page view
class SubPicture_2_ModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'sub_slug_2': ('sub_title_2',)}
    list_display = ['sub_title_2','sub_description_2','sub_video_2','sub_author_2']
admin.site.register(SubPicture_2, SubPicture_2_ModelAdmin)

#The first sub category of the detailview page view article
class VideoSubModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'video_sub_slug': ('video_sub_title',)}
    list_display = ['video_sub_title','video_sub_description','video_sub_image','video_sub_author']
admin.site.register(VideoSubImage, VideoSubModelAdmin)

#This blog is for Deus Magnus blog Page & News
class BlogDeusMagnusModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'blog_deus_magnus_slug': ('blog_deus_magnus_title',)}
    list_display = ['blog_deus_magnus_title','blog_deus_magnus_description','blog_deus_magnus_img','blog_deus_magnus_author']
admin.site.register(BlogDeusMagnus, BlogDeusMagnusModelAdmin)

#This is the event and news of Deus Magnus 
class DeusMagnusEventBlogModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'deus_magnus_event_slug': ('deus_magnus_event_title',)}
    list_display = ['deus_magnus_event_title','deus_magnus_event_description','deus_magnus_event_img',
                    'deus_magnus_event_author']
admin.site.register(DeusMagnusEventBlog, DeusMagnusEventBlogModelAdmin)

#Guides section of Deus Magnus 
class GuidesModelAdmin (admin.ModelAdmin):
    list_display = ['guides_title','guides_author','guides_img']
admin.site.register(Guides, GuidesModelAdmin)

#Our Team management of deus magnus view
class OurManagementsInDeusMagnusModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'our_team_slug': ('our_team_name',)}
    list_display = ['our_team_name','our_team_description','our_team_img','our_team_author']
admin.site.register(OurManagementsInDeusMagnus, OurManagementsInDeusMagnusModelAdmin)

# Resources FAQs of deus magnus view
class FAQsModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'FAQs_slug': ('FAQs_title',)}
    list_display = ['FAQs_title','FAQs_response','FAQs_author']
admin.site.register(FAQs, FAQsModelAdmin)

# Resources GLOSSARY of deus magnus view
class GLOSSARYModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'GLOSSARY_slug': ('GLOSSARY_title',)}
    list_display = ['GLOSSARY_title','GLOSSARY_response','GLOSSARY_author']
admin.site.register(GLOSSARY, GLOSSARYModelAdmin)

