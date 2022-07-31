# images/management/commands/createsu.py

from earthling.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email="rkawamura0483@gmail.com",
                first_name="Ryo",
                last_name="Kawamura",
                birth="2019-12-15",
                gender="男性",
                height="160",
                password='0803Kawa&!'
            )
        print('Superuser has been created.')