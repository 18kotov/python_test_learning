# -*- coding: utf-8 -*-
import unittest
from group import Group
from application import Application

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    
    def test_add_group(self):
        success = True
        self.app.open_start_page()
        self.app.login(username="admin", password="secret")
        self.app.open_groups_page()
        self.app.create_group(Group(group_name="ddfg", header="4fff", footer="fbhj"))
        self.app.return_to_groups_page()
        self.app.logout()
        self.app.assertTrue(success)

    def test_add_empty_group(self):
        success = True
        self.app.open_start_page()
        self.app.login( username="admin", password="secret")
        self.app.open_groups_page()
        self.app.create_group( Group(group_name="", header="", footer=""))
        self.app.return_to_groups_page()
        self.app.logout()
        self.app.assertTrue(success)



    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
