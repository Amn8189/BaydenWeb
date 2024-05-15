from django.contrib import admin
from .models import Event, Attendee, Subscriber, Organizer
from django.contrib.auth.admin import UserAdmin
from .forms import OrganizerCreationForm, OrganizerChangeForm  # Organizer Admin

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ("name","time_of_attendance")

class AttendeeAdmin(admin.ModelAdmin):
    model = Attendee
    list_display = ("firstname", "email")

class SubscriberAdmin(admin.ModelAdmin):
    model = Subscriber
    list_display = ("firstname", "secondname", "email")

class OrganizerAdmin(UserAdmin):
    add_form = OrganizerCreationForm
    form = OrganizerChangeForm
    model = Organizer


admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Attendee, AttendeeAdmin)


#####database$$#####
# kuazone meetup ------ identidier /- ID / Primary Key - (p.k) ------1
# iot meetup ---2