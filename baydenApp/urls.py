from django.urls import path
from .views import homepage, index, reserve, create_event, SignupView, about, contact, all_events

#Transforming method to url
urlpatterns = [
    path("", index, name="index"),
    path("reserve/<int:pk>", reserve, name="reserve"),
    path("create_event/", create_event, name="create_event"),
    path("signup/", SignupView.as_view(template_name="signup.html"), name="signup"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("all_events/", all_events, name="all_events"),
]


