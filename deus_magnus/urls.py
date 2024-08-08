
from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, SecondConstructionDetailViewArticleDetailView,VideoImageDetailView
from .views import LastConstructionDetailViewArticleDetailView, SubPictureDetailView,SubVideoDetailView
from .views import BlogArticleDetail,EventBlog,OurTeam,ManagementTeamArticleOfDuesMagnusDetail
from .views import DeusMagnusEventBlogArticleDetailView,BlogView,FAQs_item,GLOSSARY_item

urlpatterns = [
    path('index/', views.index, name='index'),
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
    path('deus_magnus_event/', EventBlog.as_view(), name='deus_magnus_event'),
    path('events_article_detail<int:pk>/', DeusMagnusEventBlogArticleDetailView.as_view(), name='events_article_detail'),
    path('our_management_team/', OurTeam.as_view(), name='our_management_team'),
    path('our_management_team_article/<int:pk>/', ManagementTeamArticleOfDuesMagnusDetail.as_view(), name="our_management_team_article"),
    path('mission_vision_strategy/', views.MissionVisionStrategesView, name='mission_vision_strategy'),
    path('founder_message/', views.FounderMessageView, name='founder_message'),
    path('services/', views.ServicesPage, name='services'),
    path('guides/', views.Guides, name='guides'),
    path('facility_management/', views.FacilityManagement, name='facility_management'),
    path('real_estate_services/', views.RealEstateServices, name='real_estate_services'),
    path('project_management/', views.ProjectManagement, name='project_management'),
    path('faqs_items/', FAQs_item.as_view(), name='faqs_items'),
    path('glossary_items/', GLOSSARY_item.as_view(), name='glossary_items'),
    
]   
