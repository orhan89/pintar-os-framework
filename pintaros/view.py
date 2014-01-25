from model import model_pool
import gtk

class View:
    _model = ''
    _columns = []
    
    def __init__(self):
        self.widget_pool = {}
        
    def get_model(self):
        global model_pool
        if(model_pool.has_key(self._model)):
            return model_pool[self._model]

    def read(self, widget=None):
        model = self.get_model()

        for item in self._columns:
            content = model.read(item)
            model._columns[item].set_value(content)

    def update(self, widget=None):
        model = self.get_model()

        for item in self._columns:
            oldValue = model.read(item)
            newValue = model._columns[item].get_value()

            if (newValue!=oldValue):
                print "Updating ",item," from ",oldValue," to ",newValue
                model.update(item, newValue)
        
    def render(self, main):
        model = self.get_model()
        
        grid = gtk.Table(rows=len(self._columns)+1, columns=2, homogeneous=gtk.FALSE)
        main.add(grid)
        grid.show()

        for idx,item in enumerate(self._columns):
            self.widget_pool[item] = model._columns[item].render()
            print self.widget_pool[item]
            grid.attach(self.widget_pool[item]['label'],0,1,idx,idx+1)

            hbox = gtk.HBox(gtk.TRUE, 0)
            for content_item in self.widget_pool[item]['content']:
                hbox.pack_start(content_item, gtk.TRUE, gtk.TRUE, 0)
            hbox.show()
            grid.attach(hbox,1,2,idx,idx+1)

        hbox = gtk.HBox(gtk.FALSE, 0)
        grid.attach(hbox,0,2,len(self._columns)+1, len(self._columns)+2)
        hbox.show()
        
        readBtn = gtk.Button(label="Read", stock=None)
        readBtn.connect("clicked", self.read)
        readBtn.show()
        hbox.pack_start(readBtn, gtk.FALSE, gtk.TRUE, 0)
        
        updateBtn = gtk.Button(label="Update", stock=None)
        updateBtn.connect("clicked", self.update)
        updateBtn.show()
        hbox.pack_start(updateBtn, gtk.FALSE, gtk.TRUE, 0)

        #self.read()

