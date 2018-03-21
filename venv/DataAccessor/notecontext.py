import sys
from venv.ObjectModel.container import Container
from venv.Storage.keyvalue_store import KeyValueStore
from venv.Storage.dynomodb import DynomoDB


class NoteContext:
    def __init__(self, store: KeyValueStore):
        self.__store = store

    def __init__(self):
        self.__store = DynomoDB.get_instance()

    def add_container(self, container: Container):
        try:
            self.__store.set(container.id, container.get_properties())
        except:
            print("Unexpected error:", sys.exc_info()[0])

    def get_containers_by_type(self, type_of: str):
        return self.__store.get("type={}".format(type_of))
