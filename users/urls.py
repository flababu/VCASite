from django.urls import path
from . import views
from users import views as users_views

urlpatterns = [
    path('profile/', users_views.profile, name='profile'),
]
