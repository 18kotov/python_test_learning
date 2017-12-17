
from model.group import Group

def test_modify_group_name(app):
    app.group.open_groups_page()
    app.group.modify_first_group(Group(group_name='New group'))
    app.group.return_to_groups_page()