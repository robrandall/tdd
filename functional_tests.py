import unittest

from selenium import webdriver


class NewViaitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()
    
    def test_start_and_retrieve_list_later(self):
        self.browser.get('http://localhost:8000')

        #header ha To-Do in it
        self.assertIn('To-Do',self.browser.title)
        self.fail('finish the test')



if __name__ == '__main__':
    unittest.main(warnings='ignore')
