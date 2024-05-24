from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Subscriber(models.Model):
    firstname = models.CharField(max_length=20)
    secondname = models.CharField(max_length=20)
    email = models.EmailField()

class Organizer(AbstractUser):
    firstname = models.CharField(max_length=20)
    secondname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

class Event(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=20, default="")
    image = models.ImageField(upload_to='Images/', blank=False)
    time_of_attendance = models.DateTimeField(default = now)
    organizer = models.ForeignKey(Organizer, models.CASCADE, default=1)

class Attendee(models.Model):
    firstname = models.CharField(max_length=50)
    secondname = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20, default="")
    job_title = models.CharField(max_length=20, default="")
    event = models.ForeignKey(Event, models.CASCADE)
    email_has_been_forwarded = models.BooleanField(default=False)
