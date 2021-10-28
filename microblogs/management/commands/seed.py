from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from microblogs.models import User

class Command(BaseCommand):
    faker = Faker('en_GB')
    def _init_(self):
        super()._init()
        self.faker = Faker('en_GB')

    def handle(self, *args,**options):
        for i in range(100):
            User.objects.create_user(username = self.faker.user_name(),
            first_name=self.faker.first_name(),
            last_name= self.faker.last_name(),
            email=self.faker.email(),
            bio="this is a faker")
