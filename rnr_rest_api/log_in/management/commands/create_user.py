from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from log_in.models import Login

class Command(BaseCommand):
    help = 'Create a user with a hashed password'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email of the new user')
        parser.add_argument('password', type=str, help='Password of the new user')

    def handle(self, *args, **kwargs):
        email = kwargs['email']
        password = kwargs['password']

        # Delete existing user if exists
        try:
            user = Login.objects.get(email=email)
            user.delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted existing user'))
        except Login.DoesNotExist:
            pass

        # Create a new user with a hashed password
        new_user = Login(email=email, password=make_password(password))
        new_user.save()
        self.stdout.write(self.style.SUCCESS('Successfully created user with hashed password'))
