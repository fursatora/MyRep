"""
URL configuration for WebCenter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.schedule, name='schedule'),
    path('groups/', views.groups, name='groups'),
    path('schedule/', views.schedule, name='schedule'),
    path('students/', views.students, name='students'),
    path('workers/', views.workers, name='workers'),

    path('students/new/', views.student_new, name='student_new'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('student/<int:pk>/add_subject/', views.add_subject_to_student, name='add_subject_to_student'),

    path('workers/new/', views.worker_new, name='worker_new'),
    path('workers/<int:pk>/', views.worker_detail, name='worker_detail'),
    path('workers/<int:pk>/edit/', views.worker_edit, name='worker_edit'),
    path('workers/<int:pk>/delete/', views.worker_delete, name='worker_delete'),

    path('groups/new/', views.group_new, name='group_new'),
    path('groups/<int:pk>/select_teacher', views.select_teacher, name='select_teacher'),
    path('groups/<int:pk>/add_students/', views.add_student_in_group, name='add_student_in_group'),
    path('groups/<int:pk>/', views.group_detail, name='group_detail'),
    path('groups/<int:pk>/delete/', views.group_delete, name='group_delete'),
    path('groups/<int:pk>/edit/', views.edit_teacher, name='edit_teacher'),

    path('groups/<int:pk>/lesson/new/', views.lesson_new, name='lesson_new'),
    path('schedule/<int:lesson_id>/', views.lesson_details, name='lesson_details'),
    path('schedule/<int:pk>/add_status/', views.add_status_to_lesson, name='add_status_to_lesson'),
    path('schedule/<int:pk>/add_students/', views.add_students_to_lesson, name='add_students_to_lesson'),
    path('schedule/<int:lesson_id>/add/info/', views.lesson_info, name='lesson_info'),
    path('schedule/<int:lesson_id>/delete/', views.delete_lesson, name='delete_lesson'),
    path('schedule/<int:lesson_id>/add/cancel/', views.lesson_cancel, name='lesson_cancel'),

]
