
from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, SecondConstructionDetailViewArticleDetailView
from .views import LastConstructionDetailViewArticleDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
    path('article2/<int:pk>/', SecondConstructionDetailViewArticleDetailView.as_view(), name="second_detail"),
    path('article3/<int:pk>/', LastConstructionDetailViewArticleDetailView.as_view(), name="last_detail"),
    path('about/', views.AboutView, name='about'),
    path('subpicture_1/', views.subpicture_1, name='subpicture_1'),
]
