from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        if self.is_superuser:
            return f"{self.username} --- SUPERUSER"
        elif self.is_staff:
            return  f"{self.username} - Staff"
        else:
            return f"{self.username}"
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to="user/profile_imgs", blank=True, null=True)
    cover_img = models.ImageField(upload_to="user/cover_imgs", blank=True, null=True)
    date_of_birth = models.DateTimeField(auto_now_add=False, blank=False, null=False)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200, blank=True, null=True)
    nationality = models.CharField(max_length=200, blank=False, null=False)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    mobile_num = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user.is_superuser:
            return f"{self.user.username} --- SUPERUSER"
        elif self.user.is_staff:
            return  f"{self.user.username} - Staff"
        return f"{self.first_name} {self.last_name} - ({self.nationality})"