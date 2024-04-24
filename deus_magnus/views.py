from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from .models import DeusMagnusMainPost, SecondDeusMagnusMainPicturePost, LastDeusMagnusMainPicturePost
from django.contrib import messages
from django.http import HttpResponse
from .models import SubPicture_1, SubPicture_2
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
    
#The second ArticleDetailView page    
class SecondConstructionDetailViewArticleDetailView(DetailView):
    model = SecondDeusMagnusMainPicturePost
    template_name = 'deus_magnus/second_article_detail.html'
    context_object_name = 'second_construction'

    def SecondConstructionDetailViewArticleDetailView(request, pk):  
        object = get_object_or_404(SecondDeusMagnusMainPicturePost, pk=pk)
        return render(request, 'deus_magnus/second_article_detail.html', {'second_detail': object})
    #This sub-model data related to the current main model instance
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subs'] = SubPicture_1.objects.all()  
        return context

#sub_picture article display inside second detailsview
class SubPictureDetailView(DetailView):
    model = SubPicture_1
    template_name = 'deus_magnus/sub_picture_detail.html'
    context_object_name = 'sub_picture'
    def SubPictureDetailView(request, pk):  
        object = get_object_or_404(SubPictureDetailView, pk=pk)
        return render(request, 'deus_magnus/sub_article_detail.html', {'sub_detail': object})
    
    
#The last sub ArticleDetailView page    
class LastConstructionDetailViewArticleDetailView(DetailView):
    model = SecondDeusMagnusMainPicturePost
    template_name = 'deus_magnus/last_article_detail.html'
    context_object_name = 'last_construction'
    
    def get(self, request, pk):  
        object = get_object_or_404(LastDeusMagnusMainPicturePost, pk=pk)
        return render(request, 'deus_magnus/last_article_detail.html', {'last_construction': object})
    
#About page of the blog
def AboutView (request):
    return render(request, 'deus_magnus/about_us.html', {})


