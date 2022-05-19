from email import message
from django.core.management.base import BaseCommand
from django.dispatch import receiver
from myproject.models import Project
from django.core.mail import send_mail
from django.conf import settings
from tabulate import tabulate


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        proj = Project()
        profiles = proj.getProfilesWhoseProjectNotUpdated()
        subject = "Not updated your projects from last 15 days."
        message_body = "Keep yourself active and update your projects on website.thank you"
        recipient = []
        for prof in profiles:
            recipient.append(prof.email)
        receiver = list(set(recipient))
        print(receiver)
        send_mail(subject, message_body, settings.EMAIL_HOST_USER, receiver)
        print('Email Send to all Profiles')
