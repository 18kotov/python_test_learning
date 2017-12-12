# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_group(app):
    app.open_start_page()
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(group_name="ddfg", header="4fff", footer="fbhj"))
    app.return_to_groups_page()
    app.logout()


def test_add_empty_group(app):
    app.open_start_page()
    app.login( username="admin", password="secret")
    app.open_groups_page()
    app.create_group( Group(group_name="", header="", footer=""))
    app.return_to_groups_page()
    app.logout()






