from . import views
from django.urls import path

urlpatterns = [
 
    path('', views.homepage ,name='home'),
    path('deleteinfo/<int:id>/', views.deleteinfo ,name='deleteinfo'),
    path('editinfo/<int:id>/', views.editinfo ,name='editinfo'),
    path('deleteinfo1/<int:id>/', views.deleteinfo1,name='deleteinfo1'),
   
]
