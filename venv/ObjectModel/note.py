from .container import Container


class Note(Container):
    def __init__(self, parent, name):
        super().__init__(parent, name)
        objects = []