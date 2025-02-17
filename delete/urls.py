from django.urls import path
from . import views

urlpatterns = [
    path('',views.search_task,name='search_task'),
    path('Delete/<str:task_name>/', views.deletetask, name="deletetask"),
]