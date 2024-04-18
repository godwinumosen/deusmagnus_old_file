from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from .models import DeusMagnusMainPost
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
    

 #The first Deus Magnus Video ArticleDetailView page
class ArticleDetailView(DetailView):
    model = DeusMagnusMainPost
    template_name = 'deus_magnus/article_detail.html'

    def ArticleDetailView(request, pk):  
        object = get_object_or_404(DeusMagnusMainPost, pk=pk)
        return render(request, 'article_detail.html', {'detail': obect})
    