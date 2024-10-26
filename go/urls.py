from django.urls import path
from .views import (restaurant_list, restaurant_create, restaurant_update, restaurant_detail,
                    restaurant_delete, place_list, place_create, place_delete, place_update, place_detail)
from . import views

urlpatterns = [
    # 1-to-1
    path('', restaurant_list, name='restaurant_list'),
    path('add/', restaurant_create, name='restaurant_create'),
    path('edit/<int:pk>/', restaurant_update, name='restaurant_update'),
    path('delete/<int:pk>/', restaurant_delete, name='restaurant_delete'),
    path('detail/<int:pk>/', restaurant_detail, name='restaurant_detail'),
    path('places/', place_list, name='place_list'),
    path('places/add/', place_create, name='place_create'),
    path('places/edit/<int:pk>/', place_update, name='place_update'),
    path('places/delete/<int:pk>/', place_delete, name='place_delete'),
    path('places/detail/<int:pk>/', place_detail, name='place_detail'),

    # 1-to-many
    path('reporters/', views.reporter_list, name='reporter_list'),
    path('reporters/create/', views.reporter_create, name='reporter_create'),
    path('reporters/<int:pk>/', views.reporter_detail, name='reporter_detail'),
    path('reporters/<int:pk>/edit/', views.reporter_edit, name='reporter_edit'),
    path('reporters/<int:pk>/delete/', views.reporter_delete, name='reporter_delete'),

    path('articles/', views.article_list, name='article_list'),
    path('articles/create/', views.article_create, name='article_create'),
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),
    path('articles/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('articles/<int:pk>/delete/', views.article_delete, name='article_delete'),

    # many-to-many
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/update/', views.student_update, name='student_update'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),

    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/<int:pk>/update/', views.course_update, name='course_update'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),
]
