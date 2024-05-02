
from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, SecondConstructionDetailViewArticleDetailView,VideoImageDetailView
from .views import LastConstructionDetailViewArticleDetailView, SubPictureDetailView,SubVideoDetailView,BlogView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
    path('article2/<int:pk>/', SecondConstructionDetailViewArticleDetailView.as_view(), name="second_detail"),
    path('article3/<int:pk>/', LastConstructionDetailViewArticleDetailView.as_view(), name="last_detail"),
    path('about/', views.AboutView, name='about'),
    path('contact/', views.ContactView, name='contact'),
    #path('subpicture_1/', views.subpicture_1, name='subpicture_1'),
    path('sub_picture/<int:pk>/', SubPictureDetailView.as_view(), name="sub_detail"),
    path('sub_video/<int:pk>/', SubVideoDetailView.as_view(), name="sub_detail_video"),
    path('sub_video_img/<int:pk>/', VideoImageDetailView.as_view(), name="sub_video_img_detail"),
    path('message/', views.message, name='message'),
    
]
