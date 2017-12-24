# -*- coding: utf-8 -*-

from model.group import Group




    
def test_add_group(app):
    app.group.open_groups_page()
    old_groups=app.group.get_group_list()
    app.group.create(Group(group_name="ddfg", header="4fff", footer="fbhj"))
    app.group.return_to_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)




def test_add_empty_group(app):
    app.group.open_groups_page()
    app.group.create(Group(group_name="", header="", footer=""))
    app.group.return_to_groups_page()







