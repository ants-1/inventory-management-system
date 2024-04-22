from django.shortcuts import render

# Create your views here.

def landing_page(request):
    return render(request, 'base/landing-page.html')

def navbar(request):
    return render(request, 'navbar.html')

def sign_up(request):
    return render(request, 'base/sign-up.html')

def login(request):
    return render(request, 'base/login.html')

def edit_profile(request):
    return render(request, 'base/edit-profile.html')

def equipment_list(request):
    return render(request, 'base/equipment-list.html')

def equipment_details(request):
    return render(request, 'base/equipment-details.html')

# User pages

def user_profile(request):
    return render(request, 'base/user-profile.html')

def user_alerts(request):
    return render(request, 'base/user-alerts.html')

def bookings(request):
    return render(request, 'base/bookings.html')

# Admin pages

def admin_profile(request):
    return render(request, 'base/admin-profile.html')

def add_equipment(request):
    return render(request, 'base/add-equipment.html')

def edit_equipement(request):
    return render(request, 'base/edit-equipment.html')

def edit_users(request):
    return render(request, 'base/edit-users.html')

def reports(request):
    return render(request, 'base/reports.html')

def approvals(request):
    return render(request, 'base/approvals.html')
