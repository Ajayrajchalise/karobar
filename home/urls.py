from django.urls import path
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('vehicles', views.vehicles, name='vehicles')
  
]
