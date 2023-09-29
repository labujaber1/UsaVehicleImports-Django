from django.urls import path
from . import views

# separate url linked to core project url for when multiple apps in project
# urlconf
urlpatterns = [
    path('Gallery/', views.createInventoryCards)  # dynamic invent cards
]
