from .crobject import CRObject
# from .dbmanage import DBmanage
from .dbpostgresql import DBPostgresql

SCHEMA = {
    'id': {
        'type': 'autoincrement',
    }, 
    'key': {
        'type': 'int',
    }, 
    'value': {
        'type': 'string',
        'max_length': 100
    }
}

class DBObjects(DBmanage):

    def __init__(self):
        super().__init__(SCHEMA, 'crobjects')

def save_crobject(self, crobject):
        data = {
                'key': crobject.key, 
                'value': crobject.value,
                }
        return self.insert(data)

def list_crobjects(self):
        list_crobjects = self.get_all()

        if not list_crobjects:
            return None

        object_crobjects = []
        # Convertimos los datos a objectos de tipo crobject
        for crobject in list_crobjects:
            c = crobject(crobject['ID'], crobject['KEY'], crobject['VALUE'])
            object_crobjects.append(c)

        return object_crobjects

    
def get_schema(self):
    return SCHEMA

def search_crobjects(self, filters):
        if not filters:
            raise ValueError('Debes envíar al menos un filtro')

        list_crobjects = self.get_by_filter(filter)
        return self._create_object_crobjects(list_crobjects)

def _create_object_crobjects(self, list_crobjects):

        if not list_crobjects:
            return None

        object_crobjects = []
        # Convertimos los datos a objectos de tipo contact
        for crobject in list_crobjects:
            c = CRObject(crobject['ID'], crobject['KEY'], crobject['VALUE'])
            object_crobjects.append(c)

        return object_crobjects

def update_crobject(self, key, value, data):
        if not key and value:
            raise ValueError('Debes enviar la key y el valor correspondiente')
        if not data:
            raise ValueError('Debes envíar al menos un parámetro a actualizar')
        self.update(key, value, data)

def delete_crobject(self, key, value):
        if not key and not value:
            raise ValueError('Debes envíar el key y el value correctos')
        self.delete(key, value)