from django.urls import path
from . import views


urlpatterns=[
    path('home',views.home,name='home'),
    path('page1',views.page1, name='page1'),
    path('aboutus',views.aboutus, name='aboutus'),
    path('css',views.css, name='css'),
    path('css2',views.css2, name='css2'),
    path('grid',views.grid, name='grid'),
    path('grid2',views.grid2, name='grid2'),
    path('bootstrap',views.bootstrap, name='bootstrap'),
    path('bootstrap2',views.bootstrap2, name='bootstrap2'),
    path('bootstrap3',views.bootstrap3, name='bootstrap3'),
    
]