from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count()==0:
        app.contact.open_add_new_page()
        app.contact.add_new(Contact("ssdr", "rr", "rrr", "ghjk", "hjj", "rrt", "tttt", "456", "rrtt@rrt.ty"))
    app.contact.delete_first_contact()