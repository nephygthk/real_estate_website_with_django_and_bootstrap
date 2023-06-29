from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView 



app_name = 'properties'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('properties/', views.AllPropertiesView.as_view(), name='properties'),
    # path('details/<slug:slug>/', views.PropertyDetailView, name='details'),
    path('details/<slug>/', views.property_details, name='details'),

    # authentication
    path('login/', views.MyLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='properties:login'),name='logout'),
    

    # crud
    path('add_property/', views.AddpropertyView.as_view(), name='add_property'),
    path('list_properties/', views.ListPropertyView.as_view(), name='list_properties'),
    path('delete_property/<pk>/', views.delete_property, name='delete_property'),
]
