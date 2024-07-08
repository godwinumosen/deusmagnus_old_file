
from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, SecondConstructionDetailViewArticleDetailView,VideoImageDetailView
from .views import LastConstructionDetailViewArticleDetailView, SubPictureDetailView,SubVideoDetailView,BlogView
from .views import BlogArticleDetail,BoardOfDirectors,BoardOfDirectorsArticleDetailView,OurTeam,ManagementTeamArticleOfDuesMagnusDetail

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
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
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog_article/<int:pk>/', BlogArticleDetail.as_view(), name="blog_detail"),
    path('board_of_director/', BoardOfDirectors.as_view(), name='bord_of_director'),
    path('board_of_director_article/<int:pk>/', BoardOfDirectorsArticleDetailView.as_view(), name="board_of_director_detail"),
    path('our_management_team/', OurTeam.as_view(), name='our_management_team'),
    path('our_management_team_article/<int:pk>/', ManagementTeamArticleOfDuesMagnusDetail.as_view(), name="our_management_team_article"),
    path('mission_vision_strategy/', views.MissionVisionStrategesView, name='mission_vision_strategy'),
    path('founder_message/', views.FounderMessageView, name='founder_message'),
    
]   
