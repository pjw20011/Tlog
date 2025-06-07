# myapp/urls.py
from django.urls import path
from .views import *
from . import views
from django.views.generic import RedirectView   

app_name = 'myapp'

urlpatterns = [ 
    path('', home_page, name='home_page'),
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
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('get_zipped_data/', views.get_zipped_data),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('home_page/', home2_page, name='home2_page'),
    path('get_name_from_db', get_name_from_db, name='get_name_from_db'),
]