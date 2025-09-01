from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings
import os


class Command(BaseCommand):
    help = 'Create a superuser for Render deployment using environment variables'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='vijayapardhu',
            help='Username for the superuser'
        )
        parser.add_argument(
            '--email',
            type=str,
            default='vijaypardhu17@gmail.com',
            help='Email for the superuser'
        )
        parser.add_argument(
            '--password',
            type=str,
            help='Password for the superuser (if not provided, will use environment variable)'
        )

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']

        # If password not provided, try to get from environment variable
        if not password:
            password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
            if not password:
                self.stdout.write(
                    self.style.ERROR(
                        'No password provided and DJANGO_SUPERUSER_PASSWORD environment variable not set. '
                        'Please set the password or provide it as an argument.'
                    )
                )
                return

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'User "{username}" already exists. Skipping creation.')
            )
            return

        if User.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.WARNING(f'User with email "{email}" already exists. Skipping creation.')
            )
            return

        try:
            # Create superuser
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created superuser "{username}" with email "{email}"'
                )
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {str(e)}')
            )
