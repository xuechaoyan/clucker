from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from microblogs.models import User

class Command(BaseCommand):
    def _init_(self):
        super()._init()

    def handle(self, *args,**options):
        for user in User.objects.all():
            if (user.username!='@admin'):
                user.delete()
