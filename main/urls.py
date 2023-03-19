from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('task/<int:pk>/',views.TaskDetailView.as_view(),name='task_detail'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>/edit/',views.TaskUpdateView.as_view(),name='edit'),
    path('task/<int:pk>/delete/',views.TaskDeleteView.as_view(),name='delete'),

]