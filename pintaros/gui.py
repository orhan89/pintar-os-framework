import pygtk
pygtk.require('2.0')
import gtk

import reader

class Gui:
    def __init__(self, models, views):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_border_width(10)
        self.window.set_usize(200,100)

        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)

        self.models = models
        self.views = views

    def run(self):
        reader.run()
        print "GUI Running..."
        for model in self.models:            
            model()
        for view in self.views:
            tmp = view()
            tmp.render(self.window)
        self.window.show()
        gtk.main()

    def delete_event(self, widget, event, data=None):
        print "GUI exited..."
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()
