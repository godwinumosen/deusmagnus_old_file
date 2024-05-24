from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from .models import DeusMagnusMainPost, SecondDeusMagnusMainPicturePost, LastDeusMagnusMainPicturePost,OurManagementsInDeusMagnus
from django.contrib import messages
from django.http import HttpResponse
from .models import SubPicture_1, SubPicture_2,VideoSubImage, BlogDeusMagnus,BoardOfDirectorsInDeusMagnus
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
    def LastConstructionDetailViewArticleDetailView(request, pk):  
        object = get_object_or_404(LastDeusMagnusMainPicturePost, pk=pk)
        return render(request, 'deus_magnus/last_article_detail.html', {'last_construction': object})
     #This sub-model data related to the last article model instance of magnus
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subs_2'] = SubPicture_2.objects.all() 
        return context
    
#About page of the deus magnus blog app..
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
        return render(request, 'deus_magnus/contact_us.html',context)

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
    
#The board of director's view
class BoardOfDirectors(ListView):
    model = BoardOfDirectorsInDeusMagnus
    template_name = 'deus_magnus/board_of_directors.html'

#The board of director's article details view
class BoardOfDirectorsArticleDetailView(DetailView):
    model = BoardOfDirectorsInDeusMagnus
    template_name = 'deus_magnus/board_of_directors_article_detail.html'
    def BoardOfDirectorsArticleDetailView(request, pk):  
        object = get_object_or_404(BoardOfDirectorsInDeusMagnus, pk=pk)
        return render(request, 'deus_magnus/board_of_directors_article_detail.html', {'board_of_directors_detail': object})
    
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