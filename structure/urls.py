from django.urls import path, include, url
from rest_framework.routers import DefaultRouter
from models.import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('resumes/', views.ResumeList.as_view()),
    path('resumes/<int:pk>/', views.ResumeDetail.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)
