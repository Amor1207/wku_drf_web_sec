from django.apps import AppConfig


class GuideConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'guide'

# Compare this snippet from wku_textbook/guide/tests.py:
# from django.test import TestCase

