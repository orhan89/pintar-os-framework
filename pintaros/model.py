from collections import OrderedDict

import math
import reader
import fields

model_pool = {}

class Model:
    _name = ''
    _fid = None

    _columns = {}

    def __init__(self):
        global model_pool
        model_pool[self._name] = self
        self._ordered_columns = OrderedDict(sorted(self._columns.items(), key=lambda t: t[0]))
        
    def install(self):
        reader.select_file(0x3f00)
        length = 0
        for item in self._columns.values():
            length += item.length
        print length
        if(reader.create_file(length, self._fid, 0x00, 0x00)):
            print "Install successfull"
            return True

    def update(self, column,  data):
        reader.select_file(self._fid)
        offset = self.get_offset(column)
        data_list = self._ordered_columns[column].format_to_card(data)
        if(reader.update_binary(offset, len(data_list), data_list)):
            print column," Updated"
            return True

    def read(self, column):
        reader.select_file(self._fid)
        offset = self.get_offset(column)
        length = self._ordered_columns[column].length
        data = reader.read_binary(offset, length)
        data_fmt = self._ordered_columns[column].format_to_terminal(data)
        print "DATA : ", str(data_fmt)
        return data_fmt

    def get_offset(self, key):
        offset = 0
        for item in self._ordered_columns:
            if (item == key):
                return offset
            else:
                offset += self._ordered_columns[item].length

