from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    role_description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    approval_status = models.ManyToManyField(User, related_name='managed_approval_status', blank=True)
    users_manage = models.ManyToManyField(User, related_name='managed_users', blank=True)
    equipment_manage = models.ManyToManyField('Equipment', related_name='managed_equipment', blank=True)
    booking_approval = models.ManyToManyField('Booking', related_name='confirmed_by_admin', blank=True)
    reservation_approval = models.ManyToManyField('Reservation', related_name='approved_by_admin', blank=True)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=254)
    # Removed catagory, on_site_date
    type = models.CharField( max_length=254)
    description = models.CharField(max_length=254)
    quantity = models.IntegerField(default=0) #Changed from equipment_count to quantity
    borrow_date = models.DateField()
    return_date = models.DateField()
    audit_date = models.DateField()
    status = models.CharField( max_length=254)
    serial_number = models.CharField( max_length=50)
    comments = models.CharField( max_length=254)
    location = models.CharField(max_length=254)
    img_url = models.CharField(max_length=254)
    availability = models.ManyToManyField(User, related_name='reserved_equipment', blank=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    booking_duration = models.DurationField() # Maybe change to DateField()
    approval_status = models.BooleanField(default=False)
    cancellation = models.BooleanField(default=False)
    rejection_reason = models.CharField(max_length=254)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    booking_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return self.name
