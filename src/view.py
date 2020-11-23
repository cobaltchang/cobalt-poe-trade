import tkinter as Tk


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


class TkinterView(View):
    title = "Cobalt PoE Trade"
    usage = """
    Use cmd + c to copy the item in PoE.
    """

    def initialize(self, master):
        master.title(self.title)
        master.geometry("600x1000+400+200")

        self.content = Tk.StringVar()
        self.content.set(self.usage)
        label = Tk.Label(master, textvariable = self.content)
        label.pack()

    def display(self):
        self.content.set(self.result)
