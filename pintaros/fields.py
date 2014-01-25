from datetime import date
import gtk
import string
import math

class CharFields:

    def __init__(self, length, name=None):
        self.length = length
        self.name = name
        self.widget = {}

    def format_to_terminal(self, content):
        data_str = ''
        for item in content:
            data_str += chr(item)
        data_str = filter(lambda x : x in string.printable, data_str)
        return data_str

    def format_to_card(self, content):
        data_list = []
        for idx in range(0,self.length):
            if(idx < len(content)):
                data_list.append(ord(content[idx]))
            else:
                data_list.append(0x0)
        return data_list

    def get_value(self):
        return self.widget['content'][0].get_text()

    def set_value(self, value):
        self.widget['content'][0].set_text(value)
        
    def render(self):
        label = gtk.Label(self.name)
        label.show()
        self.widget['label'] = label
        
        text = gtk.Entry(self.length)
        text.show()
        self.widget['content'] = [text]
        
        return self.widget

        
class SelectFields:

    def __init__(self, option, tipe, name=None):
        self.option = option
        self.length = 1
        self.tipe = tipe
        self.name = name
        self.widget = {}

    def format_to_terminal(self, content):
        data = content[0]
        return data

    def format_to_card(self, content):
        data_list = [int(content)]
        return data_list

    def get_value(self):
        if (self.tipe == 'radio'):
            for idx, radio in enumerate(self.widget['content']):
                if (radio.get_active()==1):
                    return idx

        elif (self.tipe == 'drop'):
            return self.widget['content'][0].get_active()

    def set_value(self, value):
        if (self.tipe == 'radio'):
            self.widget['content'][value].set_active(gtk.TRUE)

        elif (self.tipe == 'drop'):
            self.widget['content'][0].set_active(value)
            
    def render(self):
        label = gtk.Label(self.name)
        label.show()
        self.widget['label']=label

        if(self.tipe == 'radio'):
            self.widget['content'] = []
            radio = None
            for idx, opt in enumerate(self.option):
                radio = gtk.RadioButton(radio, opt)
                radio.show()
                self.widget['content'].append(radio)

        elif(self.tipe == 'drop'):
            drop = gtk.combo_box_new_text()
            for idx, opt in enumerate(self.option):
                print opt
                drop.append_text(opt)
            drop.show()
            
            self.widget['content'] = [drop]
            
        return self.widget

class NumberFields:

    def __init__(self, max=None, name=None):
        self.length = int(math.ceil(math.log(max,2)))
        self.name = name
        self.widget = {}

    def format_to_terminal(self, content):
        return content[0]

    def format_to_card(self, content):
        return [content]

    def get_value(self):
        return int(self.widget['content'][0].get_text())

    def set_value(self, value):
        self.widget['content'][0].set_text(str(value))

    def render(self):
        label = gtk.Label(self.name)
        label.show()
        self.widget['label']=label
        
        number = gtk.Entry(self.length)
        number.show()
        self.widget['content'] = [number]

        return self.widget

class DateFields:

    def __init__(self, name=None):
        self.length = 4
        self.name = name
        self.widget = {}

    def format_to_terminal(self, content):
        day =  content[0]
        if day == 0 : day = 1        
        month = content[1]
        if month == 0 : month = 1
        year = (content[2]<<8) + content[3]
        if year == 0 : year = 1
        return date(year,month,day)

    def format_to_card(self, content):
        data_list = [content.day, content.month, ((content.year)>>8)&0xff, (content.year)&0xff]
        return data_list

    def get_value(self):
        day = self.widget['content'][0].get_active()
        month = self.widget['content'][1].get_active()
        year = self.widget['content'][2].get_active()+1899
        
        return date(year,month,day)

    def set_value(self, value):
        self.widget['content'][0].set_active(value.day)
        self.widget['content'][1].set_active(value.month)
        self.widget['content'][2].set_active(value.year-1899)

    def render(self):
        label = gtk.Label(self.name)
        label.show()
        self.widget['label']=label

        day = gtk.combo_box_new_text()
        day.show()
        day.append_text('')
        for idx in range(1,32):
            day.append_text(str(idx))

        month_list = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
        month = gtk.combo_box_new_text()
        month.show()
        month.append_text('')
        for  item in month_list:
            month.append_text(item)

        year = gtk.combo_box_new_text()
        year.show()
        year.append_text('')        
        for idx in range(1900,2015):
            year.append_text(str(idx))
            
        self.widget['content'] = [day,month,year]

        return self.widget
