from zy2 import views
"""
URL configuration for zy project.

The urlpatterns list routes URLs to views. For more information please see:
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
from zy2 import views

from django.urls import path
from zy2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('task/', views.task, name='task'),
    path('task/addtask/', views.addtask, name='addtask'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signgin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('task/<int:task_id>/update/', views.updatetasks, name='updatetask'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('countries/', views.list_countries, name='list_countries'),  # Usar list_countries
    path('countries/add/', views.add_country, name='add_country'),
    path('countries/<int:pk>/edit/', views.update_country, name='update_country'),
    path('states/', views.list_states, name='list_states'),  # Usar list_states
    path('states/add/', views.add_state, name='add_state'),
    path('states/<int:pk>/edit/', views.update_states, name='update_states'),
]



