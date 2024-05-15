from celery import shared_task
from .models import Attendee, Event, Organizer, Subscriber
from django.core.mail import send_mail
import resend
from collections import defaultdict

RESEND_API_KEY = "re_iLx2JMc9_LALRT36DLGJ5YEFZDiCw4jbS"

@shared_task
def add_two_numbers(a, b):
    return a + b

# @shared_task
def sendmail(id):
    """ sender = "admin@baydenapp.com"
    recipient = Attendee.objects.get(pk=id)
    recipient_name = recipient.firstname
    recipient_email = recipient.email
    message = f''' Hello {recipient_name} we have recieved and forwarded ur request to attend the event.
                Thank you!!'''
    send_mail(recipient_name, message, sender, [recipient_email])
    return True """
    
    all_attendees = Attendee.objects.all().filter(email_has_been_forwarded = False)
    filtered_attendees = {}
    #{"1":[listofattendees], "2":[listofattendees], "3":[temp_attendee], "5":[att]}
    for temp_attendee in all_attendees:
        if temp_attendee.event.id in filtered_attendees.keys():
            filtered_attendees[temp_attendee.event.id].append(temp_attendee)
        else:
            filtered_attendees[temp_attendee.event.id] = [temp_attendee]
    
    attendee_dict_with_emails = defaultdict(list)
    #{1 : [.........list_of_attendees]}
    for key, val in filtered_attendees.items():
        print(key)
        print(val)
        for att in val:
            attendee_dict_with_emails[key].append[att.email]
    #{1: [attt@gmail.com, att2@ss.com]}
    for key, val in attendee_dict_with_emails.items():
        event = Event.objects.get(pk=key)
        organizer = event.organizer
        organizer_email = organizer.email
        email_message = f"Hello these are your attendees {val}"
        send_mail(organizer.firstname, email_message, "admin@bayden.com", [organizer_email])
            

    resend.api_key = RESEND_API_KEY
    r = resend.Emails.send({
    "from": "aydenmunga@gmail.com",
    "to": "bgamerboiiii@gmail.com",
    "subject": "Hello World",
    "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
})
    
@shared_task
def send_weekly_newsletters():
    all_subscribers = Subscriber.objects.all()
    all_events = Event.objects.all()
    event_details = []
    for current_ev in all_events:
        name_of_event = current_ev.name
        location_of_event = current_ev.location
        date = current_ev.time_of_attendance.strftime("%d-%m-%Y") #00-00-0000(DD-MM-YY)
        details = name_of_event + ", " + location_of_event + ", " + date + "\n"
        event_details.append(details)
    for sub in all_subscribers:
        to = sub.email
        message = f"Hello again {sub.firstname}, here are some of our events this week. \n{event_details}."
        send_mail("An update of our current events", message, "admin@bayden.com", [to])


@shared_task
def send_new_event_details():
    # todo Fetch all subscribers
    all_subs = Subscriber.objects.all()
    all_subs_emails = []
    for singlesub in all_subs:
        singlesub_email = singlesub.email
        all_subs_emails.append(singlesub_email)

    # send the new event details to all subscribers
    event = Event.objects.get(pk=id)
    name_of_event = event.name
    location_of_event = event.location
    time_of_Event = event.time_of_attendance.strftime("#d-#m-#Y")

    # Todo send the mail

    return "NEW EVENT HAS BEEN CREATED"