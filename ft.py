from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#   Keys.ENTER, Keys.Ctrl, ...
import unittest
import time

class NewUserTest(unittest.TestCase):
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

    def check_for_row_in_list_table(self, row_text):
        """
        A helper function: only methods begining in 'test' get run.
        """
        table = self.browser.find_element_by_id("id_entity_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text, [row.text for row in rows])

# Our user has heard about the double entry book keeping site
# and elects to try it out by going to the site:

    def test_can_enter_entities_and_see_them_listed(self):
        self.browser.get("http://localhost:8000")
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
        self.check_for_row_in_list_table("1. FirstEntity")
# There is still a text box allowing for creation of another.
# She creates 'SecondEntity' and sees it added to the list.
        inputbox = self.browser.find_element_by_id("id_new_entity")
        inputbox.send_keys("SecondEntity")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
# ... and sees that it appears on the page in a 'List of Entities'.
        self.check_for_row_in_list_table("1. FirstEntity")
        self.check_for_row_in_list_table("2. SecondEntity")

# Will the site remember her list??
# The site has generated a unique URL for her.

# Visiting that URL reveals her list.

# Satisfied she goes back to sleep.

        self.fail("Finish the test!")

if __name__ == '__main__':
#   unittest.main(warnings='ignore')  # launches the test runner
    unittest.main()  # launches the test runner
