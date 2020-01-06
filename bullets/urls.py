from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from bullets import views

urlpatterns = [
    path('groups/', views.GroupList.as_view()),
    path('groups/<int:pk>/', views.GroupDetail.as_view()),

    path('bullets/', views.BulletList.as_view()),
    path('bullets/<int:pk>/', views.BulletDetail.as_view()),
    

]

urlpatterns = format_suffix_patterns(urlpatterns)