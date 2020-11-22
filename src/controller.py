import time

import clipboard

from view import View


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
