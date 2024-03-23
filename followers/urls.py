from django.urls Import path
from followers import views


path('followers/', views.FollowerList.as_view()),
path('followers/<int:pk>/', views.FollowerDetail.as_view()),