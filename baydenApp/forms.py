from django.forms import Form, ModelForm, TextInput, FileInput
from django import forms
from .models import Event, Organizer
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'location', 'image', 'time_of_attendance']
        widgets = {
            'name': TextInput(attrs={
                "class": "form-control rounded-5",
                "style":"width:100%", 
        }),
            'location': TextInput(attrs={
                "class": "form-control rounded-5",
                "style":"width:100%", 
        }),
            'image': FileInput(attrs={
                "class": "form-control rounded-5",
                "style":"width:100%", 
        }),
            'time_of_attendance': TextInput(attrs={
                "class": "form-control rounded-5 text-center",
                "style":"width:100%",
        }),
        }


class SubscriberForm(Form):
    firstname = forms.CharField(max_length=20)
    secondname = forms.CharField(max_length=20)
    email = forms.EmailField()

class AttendeeForm(Form):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    email = forms.EmailField()
    company_name = forms.CharField(max_length=20)
    country = forms.CharField(max_length=20)
    job_title = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=20)

class OrganizerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Organizer
        fields = ('firstname', 'secondname', 'email', 'phone_number') + UserCreationForm.Meta.fields

class OrganizerChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Organizer
        fields = UserChangeForm.Meta.fields