
from model.group import Group

def test_edit_first_group(app):
    if app.group.count()==0:
        app.group.create(Group(group_name='test'))
    app.group.edit_first_group(Group(group_name="1234", header="gh67789k", footer="890"))

