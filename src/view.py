class View:
    result = ''

    def __init__(self, controller, model):
        self.controller = controller
        self.model = model

        self.model.register(self)

    def update(self, result):
        self.result = result
        self.display()

    def display(self):
        print(self.result)
