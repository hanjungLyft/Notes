import uuid
import datetime


class Container:
    def __init__(self, parent, name):
        self.id = uuid.uuid4()
        self.parent = parent
        self.name = name
        self.created_time = datetime.datetime.utcnow()
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_properties(self):
        properties = {}
        properties['id'] = self.id
        properties['parent'] = self.parent
        properties['name'] = self.name
        properties['created_time'] = self.created_time

        return properties
