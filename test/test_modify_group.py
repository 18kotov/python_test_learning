
from model.group import Group

def test_modify_group_name(app):
    app.open_start_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.modify_first_group(Group(group_name='New group'))
    app.group.return_to_groups_page()
    app.session.logout()