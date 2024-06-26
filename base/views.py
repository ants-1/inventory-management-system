from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from .forms import *


"""
Co-Authors:
- Anthony
- Alisha
"""

# Create your views here.


def landing_page(request):
    page_title = "Landing Page"
    return render(request, "base/landing-page.html", {"page_title": page_title})


def navbar(request):
    return render(request, "navbar.html")


def sign_up(request):
    page_title = "Sign Up"
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = AddUserForm()

    return render(request, "base/sign-up.html", {"form": form, "page_title": page_title})


def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'base/login.html', {'form':AuthenticationForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'base/login.html',
                        {'form':AuthenticationForm(),
                         'error':'Username and password invalid'})
        else:
            login(request, user)
            return redirect('equipment_list')


def logoutaccount(request):
    logout(request)
    return redirect('landing_page')


@login_required
def edit_profile(request):
    page_title = "Edit Profile"
    return render(request, "base/edit-profile.html", {"page_title": page_title})


def equipment_list(request):
    page_title = "Equipment List"
    # Get the search query 'q' from the request GET parameters, default to empty string if not provided
    q = request.GET.get("q", "")

    # Get filter values from request GET parameters or use default values if not provided
    general_filter = request.GET.get("general-filter", "all")
    type_filter = request.GET.get("type-filter", "all")
    location_filter = request.GET.get("location-filter", "all")
    status_filter = request.GET.get("status-filter", "all").lower()

    # Get all equipment items from the database
    equipment = Equipment.objects.all()

    # Apply filters based on filter values
    if general_filter == "recently-added":
        equipment = equipment.order_by("-created")
    elif general_filter == "oldest-added":
        equipment = equipment.order_by("created")

    # Apply search query filter if provided
    if type_filter != "all":
        equipment = equipment.filter(type=type_filter)
    if location_filter != "all":
        equipment = equipment.filter(location=location_filter)
    if status_filter != "all":
        equipment = equipment.filter(status__icontains=status_filter)

    if q:
        equipment = equipment.filter(
            Q(name__icontains=q)
            | Q(serial_number__icontains=q)
            | Q(description__icontains=q)
        )

    context = {
        "equipment": equipment,
        "general_filter": general_filter,
        "type_filter": type_filter,
        "location_filter": location_filter,
        "status_filter": status_filter,
        "page_title": page_title,
    }

    return render(request, "base/equipment-list.html", context)


def equipment_details(request, id):
    list_item = Equipment.objects.get(id=id)
    context = {"list_item": list_item, "page_title": list_item.name}
    return render(request, "base/equipment-details.html", context)


# User pages


def user_profile(request):
    page_title = "User Profile"
    return render(request, "base/user-profile.html", {"page_title": page_title})


def user_alerts(request):
    page_title = "User Alerts"
    return render(request, "base/user-alerts.html", {"page_title": page_title})


def bookings(request):
    page_title = "Bookings"
    return render(request, "base/bookings.html", {"page_title": page_title})


# Admin pages


def admin_profile(request):
    page_title = "Admin Profile"
    return render(request, "base/admin-profile.html", {"page_title": page_title})


def add_equipment(request):
    page_title = "Add Equipment"

    # If the request method is POST then process the form data
    if request.method == "POST":
        form = AddEquipmentForm(request.POST)
        # If the form data is valid then save it and redirect to equipment list
        if form.is_valid():
            form.save()
            return redirect("equipment_list")
    # Else the request method is GET then display a blank form
    else:
        form = AddEquipmentForm()
    return render(
        request, "base/add-equipment.html", {"form": form, "page_title": page_title}
    )


def edit_equipment(request, id):
    page_title = "Edit Equipment"
    # Retrieve the equipment object to edit based on the provided ID
    equipment = Equipment.objects.get(id=id)

    # If the request method is POST then process the form data
    if request.method == "POST":
        form = EditEquipmentForm(request.POST, instance=equipment)
        # If the form data is valid then save it and redirect to equipment list
        if form.is_valid():
            form.save()
            return redirect("equipment_list")
    # Else the request method is GET then display a blank form
    else:
        form = EditEquipmentForm(instance=equipment)
    return render(
        request, "base/edit-equipment.html", {"form": form, "page_title": page_title}
    )


def delete_equipment(request, id):
    page_title = "Delete Equipment"
    # Retrieve the equipment object to edit based on the provided ID
    equipment = Equipment.objects.get(id=id)

    # If the request method is POST then delete the equipment and redirect to equipment list
    if request.method == "POST":
        equipment.delete()
        return redirect("equipment_list")
     # If the request method is GET then display the confirmation page 
    return render(
        request,
        "base/delete-equipment.html",
        {"equipment": equipment, "page_title": page_title},
    )


def edit_users(request):
    page_title = "Edit User"
    return render(request, "base/edit-users.html", {"page_title": page_title})


def reports(request):
    page_title = "Reports"
    return render(request, "base/reports.html", {"page_title": page_title})


def approvals(request):
    page_title = "Approvals"
    return render(request, "base/approvals.html", {"page_title": page_title})
