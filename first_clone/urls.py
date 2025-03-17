"""first_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include,re_path

from blog import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #re_path(r'^accounts/profile/$',views.UserProfileView.as_view(),name='profile'),
    re_path(r'^admin/', admin.site.urls),

    re_path(r'',include('blog.urls')),
    
   # re_path(r'accounts/login/$',LoginView.as_view(template_name='registrations/login.html'),name='login'),
    #re_path(r'accounts/logout/$',LogoutView.as_view(template_name='post_list.html'),name='logout',kwargs={'next_page':'/'}),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
