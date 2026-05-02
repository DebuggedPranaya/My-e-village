"""
URL configuration for evillageproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import include, path
from application import views
from evillageproject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('agriculture/', views.agriculture, name='agriculture'),
    path('infrastructure/', views.infrastructure, name='infrastructure'),
    path('economy/', views.economy, name='economy'),
    path('contact/', views.contact, name='contact'),
    path('education/', views.education, name='education'),
    path('millbazaar/', views.millbazaar, name='millbazaar'),
    path('dashboard/index/',views.adminpage, name='adminpage'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
