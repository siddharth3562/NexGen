from django.urls import path
from . import views

urlpatterns=[
    path('home',views.user_home),
    path('courses/', views.course_list),
    path('about/', views.user_about),
    path('contacts/', views.user_contact),

]    
