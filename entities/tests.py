from django.test import TestCase
# django.test.TestCase provides client.get()
# also note: assertTemplateUsed

from django.urls import resolve
from django.http import HttpRequest
from entities.views import home_page
from entities.models import Entities, List

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

class ListViewTest(TestCase):

    def test_uses_listing_template(self):
        list_ = List.objects.create()
        response = self.client.get(f"/entities/{list_.id}/")
        self.assertTemplateUsed(response, "listing.html")

    def test_displays_only_entities_for_that_list(self):
        correct_list = List.objects.create()
        Entities.objects.create(text="FirstEntity", list=correct_list)
        Entities.objects.create(text="SecondEntity", list=correct_list)
        other_list = List.objects.create()
        Entities.objects.create(text="E1_Other", list=other_list)
        Entities.objects.create(text="E2_Other", list=other_list)

        response = self.client.get(f'/entities/{correct_list.id}/')

        self.assertContains(response, "FirstEntity")
        self.assertContains(response, "SecondEntity")
        self.assertNotContains(response, 'E1_Other')
        self.assertNotContains(response, 'E2_Other')

class ListAndEntityModelsTest(TestCase):

    def test_saving_and_retrieving_entities(self):
        list_ = List()
        list_.save()

        first_entity = Entities()
        first_entity.text = "TheFirstEntity"
        first_entity.list = list_
        first_entity.save()

        second_entity = Entities()
        second_entity.text = "TheSecondEntity"
        second_entity.list = list_
        second_entity.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Entities.objects.all()  # Query set: list like
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "TheFirstEntity")
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, "TheSecondEntity")
        self.assertEqual(second_saved_item.list, list_)
        # Above (behind the scenes) checks that id attributes match.

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

        new_list = List.objects.first()
        self.assertRedirects(response, f'/entities/{new_list.id}/')
        # The above line replaces the following 2 statements: 
#       self.assertEqual(response.status_code, 302)
#       self.assertEqual(response["location"],
#       "/entities/the_only_listing/")


# Convention being used:
# URLs without trailing slash are 'action URLs'
# - ones that modify the database.
