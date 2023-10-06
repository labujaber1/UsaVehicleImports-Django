from django.urls import path
from . import views

app_name = 'frontapp'
# separate url linked to core project url for when multiple apps in project
# urlconf
urlpatterns = [

    path('', views.home, name="Home"),

    path('Services/', views.services, name="Services"),
    path('Gallery/', views.gallery, name="Gallery"),
    path('News/', views.news, name="News"),
    path('includes/contactForm/', views.contactView, name="ContactForm"),
    path('includes/footer/', views.footerData, name="FooterData"),

    path('Success/', views.successView, name="Success"),

    path('ContactForm/', views.contactView, name="Contact2Form"),
    path('Footer/', views.footerData, name="Footer2Data"),
]
