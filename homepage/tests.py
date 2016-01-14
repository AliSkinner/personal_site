"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from homepage.models import Item


class ItemsTestCase(TestCase):
    def setUp(self):
        Item.objects.create(label="A test item", url="www.testurl.com", image="images/me.jpg", description="a test description of blah blah blah", active=True)

    def test_items_initialise_properly(self):
        test_item = Item.objects.get(label="A test item")
        self.assertEqual(test_item.url, "www.testurl.com")
