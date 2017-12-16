
from model.contact import Contact

def test_edit_first_contact(app):
    app.open_start_page()
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact("45", "12", "45", "1111", "5798", "69", "145678", "456", "rrtt@rrt.ty"))
    app.contact.go_home_page()
    app.session.logout()