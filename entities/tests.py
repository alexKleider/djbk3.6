from django.test import TestCase

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
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Entities</title>', html)
        self.assertTrue(html.endswith('</html>'))
