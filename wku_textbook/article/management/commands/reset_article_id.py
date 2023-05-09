from django.core.management.base import BaseCommand
from django.db import connection
from article.models import Article

class Command(BaseCommand):
    help = 'Reset Article ID'

    def handle(self, *args, **options):
        try:
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM sqlite_sequence WHERE name="article_article"')
            self.stdout.write(self.style.SUCCESS('Successfully reset the Article ID.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error resetting the Article ID: {e}'))
