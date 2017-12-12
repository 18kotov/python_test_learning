# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



    
def test_test_add_contact(app):
    app.open_start_page()
    app.session.login(username="admin", password="secret")
    app.open_add_new_page()
    app.add_new_contact(Contact("ssdr", "rr", "rrr", "ghjk", "hjj", "rrt", "tttt", "456", "rrtt@rrt.ty"))
    app.go_home_page()
    app.session.logout()




