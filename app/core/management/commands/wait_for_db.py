"""
Django command to wait for db to be available.
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Dajngo command to wait for db"""

    def handle(self, *args, **options):
        pass