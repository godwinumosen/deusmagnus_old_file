from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from .models import DeusMagnusMainPost, SecondDeusMagnusMainPicturePost, LastDeusMagnusMainPicturePost
from django.contrib import messages
from django.http import HttpResponse
from .models import SubPicture_1, SubPicture_2,VideoSubImage
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.urls import reverse_lazy

'''def home (request):
    return render (request, 'deus_magnus/home.html')'''

def base (request):
    return render(request,"base.html")

#The main HomeView page
class HomeView(ListView):
    model = DeusMagnusMainPost
    template_name = 'deus_magnus/home.html'

    #This model is for the second deus magnus sub category of the blog
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    #context['user'] = self.request.user
        context['second_constructions'] = SecondDeusMagnusMainPicturePost.objects.all()
    #Last deus magnus sub category of the blog for picture 
        context['last_constructions'] = LastDeusMagnusMainPicturePost.objects.all()   
        return context
    

 #The first Deus Magnus Video ArticleDetailView page
class ArticleDetailView(DetailView):
    model = DeusMagnusMainPost
    template_name = 'deus_magnus/article_detail.html'

    def ArticleDetailView(request, pk):  
        object = get_object_or_404(DeusMagnusMainPost, pk=pk)
        return render(request, 'article_detail.html', {'detail': object})
    #This is the sub-model data related to the first video model instance
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_v_imgs'] = VideoSubImage.objects.all() 
        return context
    
#The second ArticleDetailView page    
class SecondConstructionDetailViewArticleDetailView(DetailView):
    model = SecondDeusMagnusMainPicturePost
    template_name = 'deus_magnus/second_article_detail.html'
    context_object_name = 'second_construction'

    def SecondConstructionDetailViewArticleDetailView(request, pk):  
        object = get_object_or_404(SecondDeusMagnusMainPicturePost, pk=pk)
        return render(request, 'deus_magnus/second_article_detail.html', {'second_detail': object})
    #This sub-model data related to the second second model instance
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subs'] = SubPicture_1.objects.all() 
        return context
    
#The last sub ArticleDetailView page    
class LastConstructionDetailViewArticleDetailView(DetailView):
    model = LastDeusMagnusMainPicturePost
    template_name = 'deus_magnus/last_article_detail.html'
    context_object_name = 'last_construction'
    def LastConstructionDetailViewArticleDetailView(request, pk):  
        object = get_object_or_404(LastDeusMagnusMainPicturePost, pk=pk)
        return render(request, 'deus_magnus/last_article_detail.html', {'last_construction': object})
     #This sub-model data related to the last article model instance
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subs_2'] = SubPicture_2.objects.all() 
        return context
    
#About page of the blog
def AboutView (request):
    return render(request, 'deus_magnus/about_us.html', {})


#First video image sub category iterate    
class VideoImageDetailView(DetailView):
    model = VideoSubImage
    template_name = 'deus_magnus/sub_video_img_detail.html'
    context_object_name = 'sub_video_img'
    def VideoImageDetailView(request, pk):  
        object = get_object_or_404(VideoImageDetailView, pk=pk)
        return render(request, 'deus_magnus/sub_video_img_detail.html', {'sub_video_img_detail': object})
    

#sub_picture article display inside second detailsview
class SubPictureDetailView(DetailView):
    model = SubPicture_1
    template_name = 'deus_magnus/sub_picture_detail.html'
    context_object_name = 'sub_picture'
    def SubPictureDetailView(request, pk):  
        object = get_object_or_404(SubPictureDetailView, pk=pk)
        return render(request, 'deus_magnus/sub_picture_detail.html', {'sub_detail': object})
    
#sub_picture article display inside second detailsview
class SubVideoDetailView(DetailView):
    model = SubPicture_2
    template_name = 'deus_magnus/sub_video_detail.html'
    context_object_name = 'sub_video'
    def SubVideoDetailView(request, pk):  
        object = get_object_or_404(SubVideoDetailView, pk=pk)
        return render(request, 'deus_magnus/sub_video_detail.html', {'sub_detail_video': object})    

#Page Contact Us of the website
def ContactView (request):
    return render(request, 'deus_magnus/contact_us.html', {})

#This category is for the Whatsapp API for deus magnus
def whatsapp_message(request):
    whatsapp_number = '+2348066295770'
    whatsapp_link = f'https://api.whatsapp.com/send?phone={whatsapp_number}'
    context = {'whatsapp_link': whatsapp_link}
    return render(request, 'whatsapp_message.html', context)
