from typing import Any
from Blog.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This command inserts Category data"

    def handle(self, *args, **options):

        # Deleting all data
        Category.objects.all().delete()

        # List of category names
        categories = ['Sports', 'Art', 'Science', 'Technology', 'Food']

        # Creating category objects
        for category_name in categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting data!"))
