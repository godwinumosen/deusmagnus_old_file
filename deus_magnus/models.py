from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

#The search button model of locatin
    
# The main model for Deus Magnus Model category
class DeusMagnusMainPost(models.Model):
    deus_magnus_title = models.CharField(max_length=255, blank=True, null=True)
    deus_magnus_description = models.TextField()
    deus_magnus_slug = models.SlugField (max_length=255,blank=True, null=True)
    deus_manus_video = models.FileField(upload_to='videos/')
    #thumbnail = models.ImageField(max_length=100, null=True, blank=True)
    deus_magnus_publish_date = models.DateTimeField (auto_now_add= True)
    deus_magnus_author = models.ForeignKey(User, on_delete=models.CASCADE)
     
    #rent = models.CharField(max_length = 50,blank=True, null=True)

       
    class Meta:
        ordering =['-deus_magnus_publish_date']
    
    def __str__(self):
        return self.deus_magnus_title + ' | ' + str(self.deus_magnus_author)
    
    def get_absolute_url(self):
        return reverse ('home')
    
# The second model for Deus Magnus Model category
class SecondDeusMagnusMainPicturePost(models.Model):
    second_deus_magnus_title = models.CharField(max_length=255, blank=True, null=True)
    second_deus_magnus_description = models.TextField()
    second_deus_magnus_slug = models.SlugField (max_length=255,blank=True, null=True)
    second_deus_magnus_img = models.ImageField(upload_to='images/')
    second_deus_magnus_publish_date = models.DateTimeField (auto_now_add= True)
    second_deus_magnus_author = models.ForeignKey(User, on_delete=models.CASCADE)

       
    class Meta:
        ordering =['second_deus_magnus_publish_date']
    
    def __str__(self):
        return self.second_deus_magnus_title + ' | ' + str(self.second_deus_magnus_author)
    
    def get_absolute_url(self):
        return reverse ('home')
    

# The second model for Deus Magnus Model category
class LastDeusMagnusMainPicturePost(models.Model):
    last_deus_magnus_title = models.CharField(max_length=255, blank=True, null=True)
    last_deus_magnus_description = models.TextField()
    last_deus_magnus_slug = models.SlugField (max_length=255,blank=True, null=True)
    last_deus_magnus_image = models.ImageField(upload_to='images2/')
    last_deus_magnus_publish_date = models.DateTimeField (auto_now_add= True)
    last_deus_magnus_author = models.ForeignKey(User, on_delete=models.CASCADE)

       
    class Meta:
        ordering =['last_deus_magnus_publish_date']
    
    def __str__(self):
        return self.last_deus_magnus_title + ' | ' + str(self.last_deus_magnus_author)
    
    def get_absolute_url(self):
        return reverse ('home')
    
#first sub picture category of the picture
class SubPicture(models.Model):
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    sub_description = models.TextField()
    sub_slug = models.SlugField (max_length=255,blank=True, null=True)
    sub_image = models.ImageField(upload_to='images_sub/')
    sub_publish_date = models.DateTimeField (auto_now_add= True)
    sub_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['sub_publish_date']
    
    def __str__(self):
        return self.sub_title + ' | ' + str(self.sub_author)

    def get_absolute_url(self):
        return reverse('home')
    

class SubPicture_2 (models.Model):
    sub_title_2 = models.CharField(max_length=255, blank=True, null=True)
    sub_description_2 = models.TextField()
    sub_slug_2 = models.SlugField (max_length=255,blank=True, null=True)
    sub_image_2 = models.ImageField(upload_to='images_sub/')
    sub_publish_date_2 = models.DateTimeField (auto_now_add= True)
    sub_author_2 = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['sub_publish_date_2']
    
    def __str__(self):
        return self.sub_title_2 + ' | ' + str(self.sub_author_2)

    def get_absolute_url(self):
        return reverse('home')