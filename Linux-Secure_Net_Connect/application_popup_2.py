from tkinter import *


class Window(object):
    def __init__(self, master, text=None):
        self.master = master
        self.frame = Frame(master)
        self.text = text
        self.mylist = []
        # opens the popup
        button_1 = Button(
                            self.frame,
                            text='Enter IP Information',
                            command=self.open
                         )

        button_1.pack(padx=50, pady=50)

        # CLoses the application
        button_2 = Button(
                            self.frame,
                            text='Exit',
                            command=lambda: master.destroy()
                         )

        button_2.pack(pady=10)

        self.frame.pack(padx=10, pady=10)

    def open(self):
        SettingWindow(self.update)

    def update(self, var1, var2):
        self.mylist.append({"host": var1, "ip": var2})

    def return_text(self):
        # Necessary to ensure that the app returns a dictionary type
        self.frame.wait_window()
        return self.mylist


class SettingWindow:
    def __init__(self, update=None):
        self.mylist = []
        self.update = update
        self.top = Toplevel()
        self.frame = Frame(self.top)
        self.var_1 = StringVar()
        self.var_2 = StringVar()

        def display_message():
            message = self.var_1.get()
            if message:
                l_0.config(
                    text=f'User Entered {message}'
                           )

        # label to define what "entry_1" does
        l_1 = Label(
                    self.top,
                    text='Enter Hostname'
                    )
        l_1.pack()

        entry_1 = Entry(
                        self.top,
                        textvariable=self.var_1
                        )
        entry_1.pack(padx=60, pady=30)

        # label to define what "entry_1" does
        l_2 = Label(
                    self.top,
                    text='Enter IP address'
                    )
        l_2.pack()

        entry_2 = Entry(
                        self.top,
                        textvariable=self.var_2
                        )

        entry_2.pack(padx=60, pady=30)

        # button to submit and pass information unto update() method
        button_1 = Button(
                          self.top,
                          text='Submit',
                          command=lambda: [
                                            self.submit(),
                                            display_message()
                                          ]
                          )
        button_1.pack(pady=10)

        # button_2 closes the window
        button_2 = Button(
                            self.top,
                            text='Close',
                            command=lambda: self.top.destroy()
                         )

        button_2.pack(pady=10)

        l_0 = Label(
                    self.top,
                    text=' '
                    )
        l_0.pack(pady=20)

        self.frame.pack(
                        padx=10,
                        pady=10
                        )

    def submit(self):
        self.update(self.var_1.get(), self.var_2.get())
