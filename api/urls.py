# covid19helper URL Configuration

from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('<user_id>/', views.create_job, name='job'),

    path('api/category/', views.CategoryListView.as_view()),
    path('api/category/create/', views.CategoryListCreateView.as_view()),
    path('api/category/<pk>/', views.CategoryListDetailedView.as_view()),
    path('api/category/<pk>/update/', views.CategoryListUpdateView.as_view()),
    path('api/category/<pk>/delete/', views.CategoryListDeleteView.as_view()),

    path('api/job/', views.JobListView.as_view()),
    path('api/job/create/', views.JobListCreateView.as_view()),
    path('api/job/<pk>/', views.JobListDetailedView.as_view()),
    path('api/job/<pk>/update/', views.JobListUpdateView.as_view()),
    path('api/job/<pk>/delete/', views.JobListDeleteView.as_view()),

    path('api/applicant/', views.ApplicantListView.as_view()),
    path('api/applicant/create/', views.ApplicantListCreateView.as_view()),
    path('api/applicant/<pk>/', views.ApplicantListDetailedView.as_view()),
    path('api/applicant/<pk>/update/', views.ApplicantListUpdateView.as_view()),
    path('api/applicant/<pk>/delete/', views.ApplicantListDeleteView.as_view()),

    path('api/users/', views.UserListView.as_view()),
    path('api/users/create/', views.UserListCreateView.as_view()),
    path('api/users/<pk>/', views.UserListDetailedView.as_view()),
    path('api/users/<pk>/delete/', views.UserListDeleteView.as_view()),

]
