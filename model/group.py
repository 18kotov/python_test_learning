
class Group:
    def __init__(self, group_name=None, header=None, footer=None, id=None):
        self.group_name=group_name
        self.header=header
        self.footer=footer
        self.id=id


    def __repr__(self):
        return "%s:%s" % (self.id, self.group_name)

    def __eq__(self, other):
        return self.id==other.id and self.group_name==other.group_name
