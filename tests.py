"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import os
from django.test import TestCase
from django.conf import settings
from story_database.models import Site 


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        
class SiteSaveTest(TestCase):
    def test_save_site(self):
        site = Site.objects.create(domain="livinggalapagos.org")
        print os.getcwd()
        print settings.STATIC_URL
        
        
