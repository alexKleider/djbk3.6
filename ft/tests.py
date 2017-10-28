# File: ft/tests.py

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
#   Keys.ENTER, Keys.Ctrl, ...
import time

# If there are strange problems,
# try upgrading Selenium +/- geckodriver
# See ../setup.txt  (Not in the git repo.)

MAX_WAIT = 10

class NewUserTest(LiveServerTestCase):
    """
    Any method with a name beginning with 'test' is
    a test method and will be run by the test runner.
    """

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        """
        tearDown will always run unless there's an error in setUp
        """
        self.browser.close()

    def wait_for_row_in_list_table(self, row_text):
        """
        A helper function: only methods begining in 'test' get run.
        """
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id("id_entity_table")
                rows = table.find_elements_by_tag_name("tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

# Our user has heard about the double entry book keeping site
# and elects to try it out by going to the site:

    def test_can_enter_entities_and_see_them_listed(self):
        self.browser.get(self.live_server_url)
# She notices that it is a site for "Double Entry Book Keeping"...
        self.assertIn("Double Entry Book Keeping", self.browser.title)
# The home page provides her with the option of creating an 'entity'.
        header = self.browser.find_element_by_tag_name("h1")
        header_text = header.text
        self.assertIn("Entities", header_text)
        inputbox = self.browser.find_element_by_id("id_new_entity")
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            "Enter a new entity")
# She creates 'FirstEntity' ...
        inputbox.send_keys("FirstEntity")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
# ... and sees that it appears on the page in a 'List of Entities'.
        self.wait_for_row_in_list_table("1. FirstEntity")
# There is still a text box allowing for creation of another.
# She creates 'SecondEntity' and sees it added to the list.
        inputbox = self.browser.find_element_by_id("id_new_entity")
        inputbox.send_keys("SecondEntity")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
# ... and sees that it appears on the page in a 'List of Entities'.
        self.wait_for_row_in_list_table("1. FirstEntity")
        self.wait_for_row_in_list_table("2. SecondEntity")

# Will the site remember her list??
# The site has generated a unique URL for her.

# Visiting that URL reveals her list.

# Satisfied she goes back to sleep.

        self.fail("Finish the test!")

