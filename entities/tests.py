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

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
#       request = HttpRequest()
#       response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Double Entry Book Keeping</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, "home.html")
#       self.assertTemplateUsed(response, "imaginary.html")

# Test that we can deal with a POST request:

    def test_can_save_a_POST_request(self):
        """
        Since we are only testing the data base, no need to
        save the response (returned by self.client.post.)
        """
        self.client.post('/',
            data = {"entity_text": "NewEntity"})
        self.assertEqual(Entities.objects.count(), 1)
        new_entity = Entities.objects.first()
        self.assertEqual(new_entity.text, "NewEntity")

    def test_redirects_after_POST(self):
        response = self.client.post('/',
            data = {"entity_text": "NewEntity"})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"],
        "/entities/the_only_list/")

    def test_displays_all_entities(self):
        Entities.objects.create(text="FirstEntity")
        Entities.objects.create(text="SecondEntity")

        response = self.client.get('/')

        self.assertIn("FirstEntity", response.content.decode())
        self.assertIn("SecondEntity", response.content.decode())

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

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Entities.objects.count(), 0)

