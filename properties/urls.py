from django.urls import path
from . import views


app_name = 'properties'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('properties/', views.AllPropertiesView.as_view(), name='properties'),
    # path('details/<slug:slug>/', views.PropertyDetailView, name='details'),
    path('details/<slug>/', views.property_details, name='details'),
]
