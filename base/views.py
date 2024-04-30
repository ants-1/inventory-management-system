from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from .forms import *

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
    q = request.GET.get("q", "")

    general_filter = request.GET.get("general-filter", "all")
    type_filter = request.GET.get("type-filter", "all")
    location_filter = request.GET.get("location-filter", "all")
    status_filter = request.GET.get("status-filter", "all").lower()

    equipment = Equipment.objects.all()

    if general_filter == "recently-added":
        equipment = equipment.order_by("-created")
    elif general_filter == "oldest-added":
        equipment = equipment.order_by("created")

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
    }

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


def edit_equipment(request, id):
    equipment = Equipment.objects.get(id=id)
    if request.method == "POST":
        form = EditEquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect("equipment_list")
    else:
        form = EditEquipmentForm(instance=equipment)
    return render(request, "base/edit-equipment.html", {"form": form})


def delete_equipment(request, id):
    equipment = Equipment.objects.get(id=id)
    if request.method == "POST":
        equipment.delete()
        return redirect("equipment_list")
    return render(request, "base/delete-equipment.html", {"equipment": equipment})


def edit_users(request):
    return render(request, "base/edit-users.html")


def reports(request):
    return render(request, "base/reports.html")


def approvals(request):
    return render(request, "base/approvals.html")
