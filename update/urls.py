from django.urls import path
from . import views

urlpatterns = [
    path('',views.search_task_2,name='search_task_2'),
    path('UpdateTask/<str:task_name>/', views.updatetask, name="updatetask"),
]
