
from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count()==0:
        app.contact.open_add_new_page()
        app.contact.add_new(Contact("ssdr", "rr", "rrr", "ghjk", "hjj", "rrt", "tttt", "456", "rrtt@rrt.ty"))
    app.contact.edit_first_contact(Contact("45", "12", "45", "1111", "5798", "69", "145678", "456", "rrtt@rrt.ty"))
    app.contact.go_home_page()