
from model.group import Group

def test_edit_first_group(app):
    app.open_start_page()
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(group_name="1234", header="gh67789k", footer="890"))
    app.session.logout()

