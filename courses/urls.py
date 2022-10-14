from django.urls import path
from . import views             

app_name = 'courses'                

urlpatterns = [
    path('' , views.list , name='list'), 
    path('<slug:slug>/' , views.detail , name='detail'), 
    path('<slug:slug>/<int:pk>' , views.episode , name='episode'),                 
                    
]
