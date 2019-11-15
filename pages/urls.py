from django.urls import path
from . import views
from pages import views as pages_view

urlpatterns = [
    path('', views.home, name="main-home"),
    path('about/', pages_view.about , name = 'about'),
    path('contactus/' ,pages_view.contactus, name = 'contactus'),
]
