class KeyValueStore:
    __its_instance = None
    __data = {}

    @classmethod
    def get_instance(cls):
        if cls.__its_instance is None:
            cls.__its_instance = cls()

        return cls.__its_instance

    def set(self, id_of : str, properties : dict):
        self.__data[id_of] = properties

    def get(self, pattern : str):
        return self.__data