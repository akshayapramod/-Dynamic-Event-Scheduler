from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/new/', views.event_create, name='event_create'),
    path('event/<int:pk>/edit/', views.event_update, name='event_update'),
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('event/<int:event_id>/session/new/', views.session_create, name='session_create'),
    path('session/<int:pk>/edit/', views.session_update, name='session_update'),
    path('session/<int:pk>/delete/', views.session_delete, name='session_delete'),


    


]
