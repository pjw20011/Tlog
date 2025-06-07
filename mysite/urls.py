"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# mysite/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('life_graph/', life_graph, name='life_graph'),
    path('travel_graph/',travel_graph,name='travel_graph'),
    path('culture_graph/',culture_graph,name='culture_graph'),
    path('IT_graph/',IT_graph,name='IT_graph'),
    path('sports_graph/',sports_graph,name='sports_graph'),
    path('current_graph/',current_graph,name='current_graph'),
    path('wordcloud_sports/',wordcloud_sports,name='wordcloud_sports'),
    path('wordcloud_life/',wordcloud_life,name='wordcloud_life'),
    path('wordcloud_travel/',wordcloud_travel,name='wordcloud_travel'),
    path('wordcloud_IT/',wordcloud_IT,name='wordcloud_IT'),
    path('wordcloud_current/',wordcloud_current,name='wordcloud_current'),
    path('wordcloud_culture/',wordcloud_culture,name='wordcloud_culture'),
]