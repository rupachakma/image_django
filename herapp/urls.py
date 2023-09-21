from django.contrib import admin
from django.urls import path

from herapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home),
    path('view_data/', views.view_data, name="view_data"),
]
