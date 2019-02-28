import datetime
import time
import json

from os import listdir
from os.path import isfile, join

PASTE_RECORD_PATH = './records'

class PasteManager:
    def __init__(self):
        self.tables = self.load_table()

    def load_table(self):
        tables = {}
        for f in listdir(PASTE_RECORD_PATH):
             if isfile(join(PASTE_RECORD_PATH, f)):
                with open(join(PASTE_RECORD_PATH, f), 'r') as file:
                    tables[f.split('.')[0]] = json.load(file)
        return tables

    def save_table(self, table):
        with open(join(PASTE_RECORD_PATH, table + '.json'), 'w') as f:
            f.writelines(json.dumps(self.tables.get(table)))

    def save_value(self, value, table='default', name=None):
        if name is None:
            name = time.time()
        if self.tables.get(table) is None:
            self.tables[table] = {name: value}
        else:
            self.tables[table].update({name: value})
        self.save_table(table)


    def get_value(self, table='default'):
        return self.tables.get(table)
    
    def get_latest(self):
        if self.tables.get('default') is not None:
            sorted_table = sorted(self.tables['default'].items(), key=lambda kv: kv[1], reverse=True)
            latest = sorted_table[0][1]
        else:
            latest = ''
        return latest