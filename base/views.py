from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Fake DB table data to test the functionality of equipment features
""" testdata = [
    {
        "id": 1,
        "name": "Laptop w/ 2070 GPU",
        "type": "Laptop",
        "description": "Windows laptop",
        "quantity": 10,
        "borrow_date": "10-03-24",
        "return_date": "15-03-24",
        "audit_date": "20-05-24",
        "status": "On Loan",
        "serial_number": "123j1h23j42",
        "comments": "none",
        "location": "Other",
        "img_url": "base/westminster-logo.png",
    },
    {
        "id": 2,
        "name": "Laptop w/ 3070 GPU",
        "type": "Laptop",
        "description": "Windows laptop",
        "quantity": 10,
        "borrow_date": "",
        "return_date": "",
        "audit_date": "20-05-24",
        "status": "Available",
        "serial_number": "123j1h23j42",
        "comments": "none",
        "location": "Other",
        "img_url": "base/westminster-logo.png",
    },
    {
        "id": 3,
        "name": "PC w/ 4070 GPU",
        "type": "PC",
        "description": "Windows PC",
        "quantity": 10,
        "borrow_date": "",
        "return_date": "",
        "audit_date": "20-05-24",
        "status": "Out of Service",
        "serial_number": "123j1h23j42",
        "comments": "none",
        "location": "Lab 1",
        "img_url": "base/westminster-logo.png",
    },
] """

# Create your views here.

def landing_page(request):
    return render(request, "base/landing-page.html")


def navbar(request):
    return render(request, "navbar.html")


def sign_up(request):
    return render(request, "base/sign-up.html")


def login(request):
    return render(request, "base/login.html")


def edit_profile(request):
    return render(request, "base/edit-profile.html")


def equipment_list(request):
    equipment = Equipment.objects.all()
    context = {"equipment": equipment}
    return render(request, "base/equipment-list.html", context)


def equipment_details(request, id):
    list_item = Equipment.objects.get(id=id)
    context = {"list_item": list_item}
    return render(request, "base/equipment-details.html", context)


# User pages


def user_profile(request):
    return render(request, "base/user-profile.html")


def user_alerts(request):
    return render(request, "base/user-alerts.html")


def bookings(request):
    return render(request, "base/bookings.html")


# Admin pages


def admin_profile(request):
    return render(request, "base/admin-profile.html")


def add_equipment(request):
    if request.method == "POST":
        form = AddEquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equipment_list")
    else:
        form = AddEquipmentForm()
    return render(request, "base/add-equipment.html", {"form": form})


def edit_equipement(request):
    return render(request, "base/edit-equipment.html")


def edit_users(request):
    return render(request, "base/edit-users.html")


def reports(request):
    return render(request, "base/reports.html")


def approvals(request):
    return render(request, "base/approvals.html")
