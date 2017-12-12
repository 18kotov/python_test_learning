# -*- coding: utf-8 -*-
import unittest
from contact import Contact
from application import Application

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    
    def test_test_add_contact(self):
        success = True
        self.app.open_start_page()
        self.app.login(username="admin", password="secret")
        self.app.open_add_new_page()
        self.app.add_new_contact(Contact("ssdr", "rr", "rrr", "ghjk", "hjj", "rrt", "tttt", "456", "rrtt@rrt.ty"))
        self.app.go_home_page()
        self.app.logout()




    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
