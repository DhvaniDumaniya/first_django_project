"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import item_create
from myapp.views import item_list
from myapp.views import item_update
# from myapp.views import index
# from myapp.views import first
urlpatterns = [
    path('admin/', admin.site.urls),
#path('',index,name='index'),
    #path('',first,name='first')
    path('',name='thing_confrim_delete'),
    path('',name='thing_from.html'),
    path('',name='thing_list.html')
]
