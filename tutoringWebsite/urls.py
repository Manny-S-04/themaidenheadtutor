"""tutoringWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from tutor.views import index_view, reviews_view, callback_view, about_view, contactus_view, navbar,maths_view,physics_view, test_view


urlpatterns = [
    path('', index_view),
    path('admin/', admin.site.urls),
    path('index/', index_view),
    path('home/', index_view),
    path('reviews/', reviews_view, name='reviews'),
    path('callback/', callback_view, name='callbacks'),
    path('about-us/', about_view),
    path('navbar/', navbar),
    path('maths/',maths_view),
    path('physics/',physics_view),
    path('test/', test_view)
]


urlpatterns += staticfiles_urlpatterns()
