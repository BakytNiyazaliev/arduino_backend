from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings


MASTER = "Master"
STAFF = "Staff"
CUSTOMER = "Customer"



ROLES = [
    (MASTER, "Master"),
    (STAFF, "Staff"),
    (CUSTOMER, "Customer")
]

class User(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLES, default="Customer")
    objects = UserManager()
    rfid = models.CharField(max_length=40, editable=True, unique=True)



class CustomerProfile(models.Model):
    user = models.OneToOneField(User, limit_choices_to={"role":"Customer"}, on_delete=models.CASCADE)
    points = models.BigIntegerField(default=0)
    phone_number = models.CharField(max_length=20, editable=True, unique=True)
    chat_id = models.IntegerField(editable=True)

    address = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    def __str__(self) -> str:
        return self.user.username

class StaffProfile(models.Model):
    user = models.OneToOneField(User, limit_choices_to={"role":"Staff"}, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Session(models.Model):
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    points = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

    def save(self, *args, **kwargs):
        CustomerProfile.objects.filter(user=self.customer.user).update(points = models.F('points') + self.points)
        super().save(*args, **kwargs)