
from django.contrib import admin
from django.urls import path,include
from . import views



 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('addtask/',include('add.urls')),
    path('update/',include('update.urls')),
    path('display/',include('display.urls')),
    path('delete/',include('delete.urls')),
] 

