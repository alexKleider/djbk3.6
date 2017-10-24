from django.test import TestCase
# django.test.TestCase provides client.get()
# also note: assertTemplateUsed

from django.urls import resolve
from django.http import HttpRequest
from entities.views import home_page

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
        response = self.client.post('/',
            data = {"entity_text": "NewEntity"})
        self.assertIn("NewEntity", response.content.decode())
