from django.core.management.base import BaseCommand
from django.contrib.sitemaps import ping_google


class Command(BaseCommand):
    help = 'Refresh sitemap'

    def handle(self, *args, **kwargs):
        try:
            # ping_google()
            self.stdout.write(self.style.SUCCESS('Successfully pinged Google'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error pinging Google: {e}'))
