from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from .models import SubPicture_1, SubPicture_2,VideoSubImage, BlogDeusMagnus,DeusMagnusEventBlog,FAQs,Mainvideo
from .models import DeusMagnusMainPost, SecondDeusMagnusMainPicturePost,FooterPost
from .models import LastDeusMagnusMainPicturePost,OurManagementsInDeusMagnus,GLOSSARY
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin  


def index (request):
    return render (request, 'deus_magnus/index.html')

def base_view(request):
    try:
        footer_post = FooterPost.objects.latest('id')  # Fetch the most recent footer post
    except FooterPost.DoesNotExist:
        footer_post = None

    return render(request, 'base.html', {'footer_post': footer_post})

#The main HomeView page
class HomeView(ListView): 
    model = DeusMagnusMainPost
    template_name = 'deus_magnus/home.html'

    #This model is for the second deus magnus sub category of the blog
    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
    #the first deus magnus home video
        context['first_videos'] = Mainvideo.objects.all()    
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
    
#The second ArticleDetailView page of deus magnus group   
class SecondConstructionDetailViewArticleDetailView(DetailView):
    model = SecondDeusMagnusMainPicturePost
    template_name = 'deus_magnus/second_article_detail.html'    
    context_object_name = 'second_construction'

    def SecondConstructionDetailViewArticleDetailView(request, pk):    
        object = get_object_or_404(SecondDeusMagnusMainPicturePost, pk=pk)
        return render(request, 'deus_magnus/second_article_detail.html', {'second_detail': object})
    #This sub-model data related to the second article model instance in deus magnus group
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subs'] = SubPicture_1.objects.all() 
        return context

#The last sub ArticleDetailView page    
class LastConstructionDetailViewArticleDetailView(DetailView):
    model = LastDeusMagnusMainPicturePost
    template_name = 'deus_magnus/last_article_detail.html'
    context_object_name = 'last_construction'
    def LastConstructionDetailViewArticleDetailView(request, pk)
        object = get_object_or_404(LastDeusMagnusMainPicturePost, pk=pk)
        return render(request, 'deus_magnus/last_article_detail.html', {'last_construction': object})
     #This sub-model data related to the last article model instance of magnus
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subs_2'] = SubPicture_2.objects.all() 
        return context
    
# About page of  the deus magnus blog app
def AboutView (request):
    return render(request, 'deus_magnus/about_us.html', {})
# Services page of the deus magnus webapp
def ServicesPage (request):
    return render(request, 'deus_magnus/servicespage.html', {})
# Facility Management page of the deus magnus webapp
def FacilityManagement (request):
    return render(request, 'deus_magnus/facility_management.html', {})
# Real Estate Services page of the deus magnus webapp
def RealEstateServices (request):
    return render(request, 'deus_magnus/real_estate_services.html', {})
# Project Management page of the deus magnus webapp
def ProjectManagement (request):
    return render(request, 'deus_magnus/project_management.html', {})
# Guides Management page of the deus magnus webapp
def Guides (request):
    return render(request, 'deus_magnus/guides.html', {})
# Construction Development Management page of the deus magnus webapp
def ConstructionDevelopment (request):
    return render(request, 'deus_magnus/construction_development.html', {})

# The frequently ask qeustion page of the media dropdown
class FAQs_item(ListView):
    model = FAQs
    template_name = 'deus_magnus/faqs.html'
    context_object_name = 'faqs_items'

# The GLOSSARY page of the media dropdown
class GLOSSARY_item(ListView):
    model = GLOSSARY
    template_name = 'deus_magnus/glossary.html'
    context_object_name = 'glossary_items'


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
        return render(request, 'deus_magnus/sub_video_detail.html', {'sub_detail_video':object}) 

#This category is for the Whatsapp API for deus magnus
def deus_magnus_whatsapp_message(request):
    deus_magnus_whatsapp_number = '+2348066295770'
    dues_magnus_whatsapp_link = f'https://api.whatsapp.com/send?phone={deus_magnus_whatsapp_number}'
    context = {'whatsapp_link': dues_magnus_whatsapp_link}
    return render(request, 'deus_magnus_kwhatsapp_message.html', context)

# The Contact view been implemented
def ContactView (request):
    email='info@deusmagnus.com'
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message'] 
        messages.success(request, f'Your email was Successfully sent to Deus Magnus {message_name}..!')
        return redirect('/message')
    else:
        context={
            'email':email
        } 
        return render(request, 'deus_magnus/contact_us.html', {})

def message (request):
    return render (request, 'deus_magnus/message.html', {})

#This is the blog services category of deus magnus
class BlogView(ListView):
    model = BlogDeusMagnus
    template_name = 'deus_magnus/blog.html'
    
#The blog article of the blog project of Deus Magnus
class BlogArticleDetail(DetailView):
    model = BlogDeusMagnus
    template_name = 'deus_magnus/blog_article_detail.html'

    def BlogArticleDetail(request, pk):  
        object = get_object_or_404(BlogDeusMagnus, pk=pk)
        return render(request, 'deus_magnus/blog_article_detail.html', {'blog_detail': object})
    
#This article belong to deus_magnus_events view
class EventBlog(ListView):
    model = DeusMagnusEventBlog
    template_name = 'deus_magnus/deus_magnus_events.html'

#The event of deus magnus' article details class base view
class DeusMagnusEventBlogArticleDetailView(DetailView):
    model = DeusMagnusEventBlog
    template_name = 'deus_magnus/deus_magnus_event_article.html'
    def DeusMagnusEventBlogArticleDetailView(request, pk): 
        object = get_object_or_404(DeusMagnusEventBlog, pk=pk)
        return render(request, 'deus_magnus/deus_magnus_event_article.html',{'events_article_detail': object})
    
#Our Team management of deus magnus view
class OurTeam(ListView):
    model = OurManagementsInDeusMagnus
    template_name = 'deus_magnus/our_team.html'

#the management team article of dues magnus details views
class ManagementTeamArticleOfDuesMagnusDetail(DeleteView):
    model = OurManagementsInDeusMagnus 
    template_name = 'deus_magnus/our_team_article_detail.html'
    def ManagementTeamArticleOfDuesMagnusDetail(request, pk):
        object = get_object_or_404(OurManagementsInDeusMagnus, pk=pk)
        return render (request, 'dues_magnus/our_team_article_detail.html',{'our_management_team_article': object})
    
def MissionVisionStrategesView (request):
    return render (request, 'deus_magnus/mission_vision.html', {})

def FounderMessageView (request):
    return render(request, 'deus_magnus/founder_message.html', {}) 