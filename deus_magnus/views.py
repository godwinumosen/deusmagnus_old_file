from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from .models import DeusMagnusMainPost, SecondDeusMagnusMainPicturePost
from django.contrib import messages
from django.http import HttpResponse
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