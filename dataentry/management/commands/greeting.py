from django.core.management.base import BaseCommand, CommandParser

#Proposed command = python manage.py greeting John
#proposed output = Hi {name}, Good Morning
class Command(BaseCommand):
    help = 'Greets the User'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies user name')


    def handle(self, *args, **kwargs):
        # Write the logic
        name = kwargs ['name']
        greeting = f'Hi {name}, Good Morning'
        self.stdout.write(self.style.SUCCESS(greeting))#for green in color
        self.stderr.write(greeting)#for red in color
        self.stdout.write(greeting)#for white in color
        self.stdout.write(self.style.WARNING(greeting))#for yellow in color