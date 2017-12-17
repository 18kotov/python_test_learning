# -*- coding: utf-8 -*-

from model.contact import Contact

    
def test_add_contact(app):
    app.contact.open_add_new_page()
    app.contact.add_new(Contact("ssdr", "rr", "rrr", "ghjk", "hjj", "rrt", "tttt", "456", "rrtt@rrt.ty"))
    app.contact.go_home_page()





