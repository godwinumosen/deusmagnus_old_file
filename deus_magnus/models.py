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

       
    class Meta:
        ordering =['-deus_magnus_publish_date']
    
    def __str__(self):
        return self.deus_magnus_title + ' | ' + str(self.deus_magnus_author)
    
    def get_absolute_url(self):
        return reverse('home','sub_video_img_detail','sub_detail_video','sub_detail',
                       'board_detail','blog_detail','last_detail','second_detail','detail')
    
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
        return reverse('home','sub_video_img_detail','sub_detail_video','sub_detail',
                       'board_detail','blog_detail','last_detail','second_detail','detail')
    

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
        return reverse('home','sub_video_img_detail','sub_detail_video','sub_detail',
                       'board_detail','blog_detail','last_detail','second_detail','detail')
    
#first sub picture category of the picture
class SubPicture_1(models.Model):
    sub_title_1 = models.CharField(max_length=200, blank=True, null=True)
    sub_description_1 = models.TextField()
    sub_slug_1 = models.SlugField (max_length=255,blank=True, null=True)
    sub_image_1 = models.ImageField(upload_to='images_sub/'
    sub_publish_date_1 = models.DateTimeField (auto_now_add= True)
    sub_author_1 = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['sub_publish_date_1']
    
    def __str__(self):
        return self.sub_title_1 + ' | ' + str(self.sub_author_1)

    def get_absolute_url(self):
        return reverse('home','sub_video_img_detail','sub_detail_video','sub_detail',
                       'board_detail','blog_detail','last_detail','second_detail','detail')
    

class SubPicture_2 (models.Model):
    sub_title_2 = models.CharField(max_length=255, blank=True, null=True)
    sub_description_2 = models.TextField()
    sub_slug_2 = models.SlugField (max_length=255,blank=True, null=True)
    #sub_image_2 = models.ImageField(upload_to='images_sub/')
    sub_video_2 = models.FileField(upload_to='video_sub/')
    sub_publish_date_2 = models.DateTimeField (auto_now_add= True)
    sub_author_2 = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['sub_publish_date_2']
    
    def __str__(self):
        return self.sub_title_2 + ' | ' + str(self.sub_author_2)

    def get_absolute_url(self):
        return reverse('home','sub_video_img_detail','sub_detail_video','sub_detail',
                       'board_detail','blog_detail','last_detail','second_detail','detail')
    
    
#first sub video category of the video
class VideoSubImage(models.Model):
    video_sub_title = models.CharField(max_length=200, blank=True, null=True)
    video_sub_description = models.TextField()
    video_sub_slug = models.SlugField (max_length=255,blank=True, null=True)
    video_sub_image = models.ImageField(upload_to='video_sub_images/')
    video_sub_publish_date = models.DateTimeField (auto_now_add= True)
    video_sub_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['video_sub_publish_date']
    
    def __str__(self):
        return self.video_sub_title + ' | ' + str(self.video_sub_author)

    def get_absolute_url(self):
        return reverse('home','sub_video_img_detail','sub_detail_video',
                       'board_detail','blog_detail','sub_detail','last_detail','second_detail','detail')
    
#The blog category
class BlogDeusMagnus(models.Model):
    blog_deus_magnus_title = models.CharField(max_length=255, blank=True, null=True)
    blog_deus_magnus_description = models.TextField()
    blog_deus_magnus_slug = models.SlugField (max_length=255,blank=True, null=True)
    blog_deus_magnus_img = models.ImageField(upload_to='blog_images/')
    blog_deus_magnus_publish_date = models.DateTimeField (auto_now_add= True)
    blog_deus_magnus_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['-blog_deus_magnus_publish_date']
    
    def __str__(self):
        return self.blog_deus_magnus_title + ' | ' + str(self.blog_deus_magnus_author)
    
    def get_absolute_url(self):
        return reverse('home','sub_video_img_detail','sub_detail_video','sub_detail',
                       'last_detail','second_detail','detail','board_detail','blog_detail',)

#The board of director's view 
class BoardOfDirectorsInDeusMagnus(models.Model):
    board_of_directos_name = models.CharField(max_length=255, blank=True, null=True)
    board_of_directos_position = models.CharField(max_length=255, blank=True, null=True)
    board_of_directos_description = models.TextField()
    board_of_directos_slug = models.SlugField (max_length=255,blank=True, null=True)
    board_of_directos_img = models.ImageField(upload_to='directors_images/')
    board_of_directos_author = models.ForeignKey(User, on_delete=models.CASCADE)
    board_of_directos_publish_date = models.DateTimeField (auto_now_add= True)

    class Meta:
        ordering =['-board_of_directos_publish_date']
    
    def __str__(self):
        return self.board_of_directos_name + ' | ' + str(self.board_of_directos_author)
    
    def get_absolute_url(self):
        return reverse('home','sub_video_img_detail','sub_detail_video','sub_detail','last_detail',
                       'second_detail','detail','board_detail','blog_detail',)


#Our Team management of deus magnus view
class OurManagementsInDeusMagnus(models.Model):
    our_team_name = models.CharField(max_length=255, blank=True, null=True)
    our_team_position = models.CharField(max_length=255, blank=True, null=True)
    our_team_description = models.TextField()
    our_team_slug = models.SlugField (max_length=255,blank=True, null=True)
    our_team_img = models.ImageField(upload_to='our_team_images/')
    our_team_author = models.ForeignKey(User, on_delete=models.CASCADE)
    our_team_publish_date = models.DateTimeField (auto_now_add= True)

    class Meta:
        ordering =['-our_team_publish_date']
    
    def __str__(self):
        return self.our_team_name + ' | ' + str(self.our_team_author)
    
    def get_absolute_url(self):
        return reverse('home','sub_video_img_detail','sub_detail_video','sub_detail','last_detail',
                       'second_detail','detail','board_detail','blog_detail',)
