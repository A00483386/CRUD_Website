from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),  # 为根 URL 定义视图
    path('create_student/', views.create_student, name='create_student'),
    path('view_students/', views.view_students, name='view_students'),

    path('create_student/', views.create_student, name='create_student'),
    path('view_students/', views.view_students, name='view_students'),
    path('update_student/<str:student_id>/', views.update_student, name='update_student'),
    path('delete_student/<str:student_id>/', views.delete_student, name='delete_student'),
    # 添加其他实体的 CRUD 路由

    path('create_support_service/', views.create_support_service, name='create_support_service'),
    path('view_support_services/', views.view_support_services, name='view_support_services'),
    path('update_support_service/<int:service_id>/', views.update_support_service, name='update_support_service'),
    path('delete_support_service/<int:service_id>/', views.delete_support_service, name='delete_support_service'),

    # 其他路由
    path('create_appointment/<int:service_id>/', views.create_appointment, name='create_appointment'),
    
    path('view_appointments/', views.view_appointments, name='view_appointments'),
    
    path('create_feedback/', views.create_feedback, name='create_feedback'),
    path('view_feedbacks/', views.view_feedbacks, name='view_feedbacks'),

]