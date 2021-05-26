"""crud URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from register import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home, name='home_index'),
    path('project', views.add_show, name="add&show"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
    path('signup/',views.sign_up, name="signup"),
    path('login/',views.user_login, name="login"),
    path('profile/',views.user_profile, name="profile"),
    path('logout/',views.user_logout, name="logout"),
    path('news/',views.news, name='news'),
    path('changepass/',views.changepass, name="changepass"),
    path('', include('register.urls')),
    #path('discussion/',views.discussion, name='discussion'),
    #path('changepass/',views.user_changepass, name="changepass"),
    #path('news/',views.news, name='news'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
