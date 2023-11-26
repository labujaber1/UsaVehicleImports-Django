
from django.urls import path
from . import views

app_name = 'frontapp'
# separate url linked to core project url for when multiple apps in project
# urlconf
urlpatterns = [

    path('', views.HomeView.as_view(), name="Home"),
    
    path('Services/', views.ServicesView.as_view(), name="Services"),
    path('Gallery/', views.Gallery.as_view(), name="Gallery"),
    path('News/', views.News.as_view(), name="News"),
    path('Success/', views.SuccessView.as_view(), name="Success"),
    path('Error404/', views.Error404View.as_view(), name="Error404"),
    path('includes/contactForm/', views.processContactFormView, name="ContactForm"),
    path('includes/footer/', views.FooterListView.as_view(), name="FooterData"), 
    path('includes/commentsForm/<uuid:id>', views.CommentOnPostView.as_view(), name="CommentOnPost"),
    path('News/<uuid:id>', views.News.as_view(), name="LikePost"),
    
    
]   
