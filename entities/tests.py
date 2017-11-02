from django.test import TestCase
# django.test.TestCase provides client.get()
# also note: assertTemplateUsed

from django.urls import resolve
from django.http import HttpRequest
from entities.views import home_page
from entities.models import Entities

# Create your tests here.

# Want to test at least 3 things:
# 1. can we resolve URL for site root ("/") to a particular view
# function?
# 2. can we make this view function return some html with which to get
# the functional test to pass?

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'home.html')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Entities.objects.count(), 0)

class ListViewTest(TestCase):

    def test_uses_listing_template(self):
        response = self.client.get("/entities/the_only_listing/")
        self.assertTemplateUsed(response, "listing.html")

    def test_displays_all_entities(self):
        Entities.objects.create(text="FirstEntity")
        Entities.objects.create(text="SecondEntity")

        response = self.client.get('/entities/the_only_listing/')

        self.assertContains(response, "FirstEntity")
        self.assertContains(response, "SecondEntity")

class EntityModelTest(TestCase):

    def test_saving_and_retrieving_entities(self):
        first_entity = Entities()
        first_entity.text = "TheFirstEntity"
        first_entity.save()

        second_entity = Entities()
        second_entity.text = "TheSecondEntity"
        second_entity.save()

        saved_items = Entities.objects.all()  # Query set: list like
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "TheFirstEntity")
        self.assertEqual(second_saved_item.text, "TheSecondEntity")

class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        """
        Since we are only testing the data base, no need to
        save the response (returned by self.client.post.)
        """
        self.client.post('/entities/new',
            data = {"entity_text": "NewEntity"})
        self.assertEqual(Entities.objects.count(), 1)
        new_entity = Entities.objects.first()
        self.assertEqual(new_entity.text, "NewEntity")

    def test_redirects_after_POST(self):
        response = self.client.post('/entities/new',
            data = {"entity_text": "NewEntity"})

        self.assertRedirects(response, '/entities/the_only_listing/')
        # The above line replaces the following 2 statements: 
#       self.assertEqual(response.status_code, 302)
#       self.assertEqual(response["location"],
#       "/entities/the_only_listing/")


# Convention being used:
# URLs without trailing slash are 'action URLs'
# - ones that modify the database.
