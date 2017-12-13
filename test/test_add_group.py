# -*- coding: utf-8 -*-

from model.group import Group




    
def test_add_group(app):
    app.open_start_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(group_name="ddfg", header="4fff", footer="fbhj"))
    app.group.return_to_groups_page()
    app.session.logout()


def test_add_empty_group(app):
    app.open_start_page()
    app.session.login( username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(group_name="", header="", footer=""))
    app.group.return_to_groups_page()
    app.session.logout()






