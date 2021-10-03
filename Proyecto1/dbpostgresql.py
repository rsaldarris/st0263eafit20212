import psycopg2
import re
from environs import Env
import mysql.connector

class DBPostgresql:

    def __init__(self, schema, table_name):
        self._table_name = table_name
        self._schema = schema
        env = Env()
        env.read_env()
        # self._connect = mysql.connector.connect(
        self._connect = psycopg2.connect(
            host=env('POSTGRES_HOST'), 
            database=env('POSTGRES_DB'), 
            user=env('POSTGRES_USER'), 
            password=env('POSTGRES_PASSWORD')
        )

        self._cur = self._connect.cursor()
        self._launch_query('SELECT 1')
        print('Conexión establecida con éxito')
            
        self._create_table()

    def _create_table(self):

        query = f'CREATE TABLE IF NOT EXISTS public.{self._table_name} ('
        primary_key = ''
        for field_name, config in self._schema.items():
            if config['type'] == 'autoincrement':
                query += f'{field_name} serial,'
                primary_key = f'PRIMARY KEY ({field_name})'

            elif config['type'] in ['string', 'int']:
                if config['type'] == 'string':
                    query += f'{field_name} character varying'
                else:
                    query += f'{field_name} integer'

                if 'max_length' in config:
                    query += f'({config["max_length"]})'
                query += ','

        query += f'{primary_key})'

        self._launch_query(query)
    
    def _launch_query(self, query):
        print(query)
        self._cur.execute(query)
        matches = re.search(r"^SELECT", query, re.IGNORECASE)
        if not matches:
            self._connect.commit()

    def __del__(self):
        self._connect.close()
        self._cur.close()

    def insert(self, data):

        values = "'" + "', '".join(str(x) for x in data.values()) + "'"
        query = f'INSERT INTO public.{self._table_name} ({", ".join(str(x) for x in data.keys())}) VALUES ({values});'

        self._launch_query(query)

        return True

    def update(self, crkey, crvalue, data):

        list_update = []
        for field_name, field_value in data.items():
            if field_name == "KEY":
                list_update.append(f"{field_name}={field_value}")
            else:
                list_update.append(f"{field_name}='{field_value}'")
        

        query = f'UPDATE public.{self._table_name} SET {", ".join(list_update)} WHERE key = {crkey} AND value = \'{crvalue}\';'
        self._launch_query(query)

    def delete(self, crkey, crvalue):
        query = f'DELETE FROM public.{self._table_name} WHERE key = {crkey} AND value = \'{crvalue}\';'

        self._launch_query(query)
    
    def get_by_key_value(self, crkey, crvalue):
        query = f'SELECT * FROM public.{self._table_name} WHERE key = {crkey} AND key = {crvalue};'

        table_keys = []
        for schema_key in self._schema.keys():
            table_keys.append(schema_key)
            
        data = {}
        self._launch_query(query)
        row = self._cur.fetchone()
        for key, value in enumerate(row):
            data[table_keys[key]] = value

        return data

    def get_by_filters(self, key=None):

        list_filters = []
        
        where = '1=1'
        if key is not None:
            for field_value in key:
                list_filters.append(f"key = {field_value}")

                where = " AND ".join(list_filters)
            # where = f"key = {key}"


        query = f'SELECT * FROM public.{self._table_name} WHERE {where};'

        table_keys = []
        for schema_key in self._schema.keys():
            table_keys.append(schema_key)

        list_data = []
        self._launch_query(query)
        rows = self._cur.fetchall()

        for row in rows:
            data = {}
            for key, value in enumerate(row):
                data[table_keys[key]] = value

            list_data.append(data)

        return list_data

    def get_all(self):
        return self.get_by_filters()