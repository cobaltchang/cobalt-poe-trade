class Observable:
    observers = []

    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)


class Model(Observable):
    item = ''

    def notify(self):
        for observer in self.observers:
            observer.update(self.item)

    def set_item(self, copied_item):
        self.item = copied_item
        self.notify()
