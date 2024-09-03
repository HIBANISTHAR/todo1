from django.urls import path
from.import views
urlpatterns=[
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('todo',views.todo1,name='todo'),
    path('deltodo/<int:id>',views.deltodo,name='deltodo'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('about',views.about,name='about'),


]