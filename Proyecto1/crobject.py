class CRObject:
    def __init__(self, id_crobject, key, value):
        self._id_crobject = id_crobject
        self._key = key
        self._value = value

    def getkey(self):
        return self._key

    def setkey(self, key):
        self._key = key

    def getvalue(self):
        return self._value

    def setvalue(self, value):
        self._value = value

    def getid(self):
        return self._id_crobject

    def setid(self, id_crobject):
        self._id_crobject = id_crobject
