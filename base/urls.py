from django.urls import path
from . import views



urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('landing_page', views.landing_page, name='landing_page'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('login', views.login, name='login'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('equipment_details/<int:id>/', views.equipment_details, name='equipment_details'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('user_alerts', views.user_alerts, name='user_alerts'),
    path('bookings', views.bookings, name='bookings'),
    path('admin_profile', views.admin_profile, name='admin_profile'),
    path('add_equipment', views.add_equipment, name='add_equipment'),
    path('edit_equipment', views.edit_equipement, name='edit_equipment'),
    path('edit_users', views.edit_users, name='edit_users'),
    path('reports', views.reports, name='reports'),
    path('approvals', views.approvals, name='approvals'),
    path('equipment_list', views.equipment_list, name="equipment_list"),
]
