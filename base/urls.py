from django.urls import path
from . import views



urlpatterns = [
    path('', views.landing_page, name='base_landing_page'),
    path('sign_up', views.sign_up, name='base_sign_up'),
    path('login', views.login, name='base_login'),
    path('edit_profile', views.edit_profile, name='base_edit_profile'), # Form
    path('equipment_details', views.equipment_details),
    path('user_profile', views.user_profile, name='base_user_profile'),
    path('user_alerts', views.user_alerts, name='base_user_alerts'),
    path('bookings', views.bookings, name='base_bookings'),
    path('admin_profile', views.admin_profile, name='base_admin_profile'),
    path('add_equipment', views.add_equipment, name='base_add_equipment'),
    path('edit_equipment', views.edit_equipement, name='base_edit_equipment'),
    path('edit_users', views.edit_users, name='base_edit_users'),
    path('reports', views.reports, name='base_reports'),
    path('approvals', views.approvals, name='base_approvals')
]
