from tkinter import *
from application_popup_2 import Window as Win


class Main_Window(Win):
    def __init__(self, master):
        self.master = master
        self.win = Toplevel(master)
        super().__init__(self.win)  # is used to inherit from another class "Window()"

    # Return dictionary with IP information {'host': , 'ip'}
    def main(self):
        return super().return_text()
