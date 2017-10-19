from selenium import webdriver
import unittest

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

# Our user has heard about the double entry book keeping site
# and elects to try it out by going to the site:

    def test_can_enter_entities_and_see_them_listed(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("Entities", self.browser.title)
        self.fail("Finish the test!")

# The home page provides her with the option of creating
# an 'entity'.

# She creates 'FirstEntity' and sees that it appears on the page
# in a 'List of Entities'.

# There is still a text box allowing for creation of another.
# She creates 'SecondEntity' and sees it added to the list.

# Will the site remember her list??
# The site has generated a unique URL for her.

# Visiting that URL reveals her list.

# Satisfied she goes back to sleep.

if __name__ == '__main__':
#   unittest.main(warnings='ignore')  # launches the test runner
    unittest.main()  # launches the test runner
