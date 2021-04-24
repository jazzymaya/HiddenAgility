"""ebdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
from ebdjango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.NewHomepage, name = 'NewHome'),
    path('Upload', views.NewUploadpage, name = 'NewUpload'),
    path('NewFAQ', views.NewFAQpage, name = 'NewFAQ'),
    path('AboutUs', views.NewAboutUspage, name = 'NewAboutUs'),
    path('Results', views.NewResultspage, name='NewResults'),
    path('AdvancedPinkeye', views.AdvancedPinkeye, name='AdvancedPinkeye'),
    path('AdvancedChickenpox', views.AdvancedChickenpox, name='AdvancedChickenpox'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)