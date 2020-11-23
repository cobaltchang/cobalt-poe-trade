import time
import tkinter as Tk

import clipboard

from view import TkinterView, View


class Controller:

    def __init__(self, model):
        self.model = model
        self.view = View(self, self.model)

    def run(self):
        while True:
            self.detect_copied()
            time.sleep(1)

    def detect_copied(self):
        copied = clipboard.paste()
        if self.is_item(copied):
            clipboard.copy('')
            self.model.set_item(copied)

    def is_item(self, copied):
        if copied:
            if copied.startswith('Rarity: ') and '--------' in copied:
                return True


class TkinterController(Controller):

    def __init__(self, model):
        self.model = model
        self.view = TkinterView(self, self.model)

        self.window = Tk.Tk()
        self.view.initialize(self.window)

    def run(self):
        self.window.after(1000, self.detect_copied)
        self.window.mainloop()

    def detect_copied(self):
        super().detect_copied()
        self.window.after(1000, self.detect_copied)
