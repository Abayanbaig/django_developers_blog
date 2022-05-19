from django.core.management.base import BaseCommand
from myproject.models import Project


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        proj = Project()
        proj.status()
