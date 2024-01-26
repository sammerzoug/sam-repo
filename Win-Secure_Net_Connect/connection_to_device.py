from tkinter import *
from tkinter import font as tkFont
from netmiko import ConnectHandler
import tkinter
import time


# this dictionary is used to capture {'username': 'user', 'password': 'pass'}
mydict = {}


class credential(object):
    def __init__(self, win):
        self.win = Toplevel(win)
        self.win.geometry('500x300')
        self.frame = Frame(self.win)
        self.helv36 = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)
        self.var_1 = StringVar()
        self.var_2 = StringVar()
        self.mydict = dict()

        # Create a text label
        Label(self.frame,
              text="Enter Device Credentials",
              font=('Helvetica', 20)
              ).pack(pady=20)

        # Create Entry Widget for username
        username = Entry(
            self.frame,
            width=20,
            font=self.helv36,
            textvariable=self.var_1
        )
        username.pack()

        # Create Entry Widget for password
        password = Entry(
            self.frame,
            font=self.helv36,
            show="*",
            width=20,
            textvariable=self.var_2
        )
        password.pack()

        # Create a button to close the window
        Button(
               self.frame,
               text="Submit",
               font=('Helvetica bold', 15),
               command=lambda: [
                                self.submit(),
                                self.close_win()
                                ]
               ).pack(pady=5)

        self.frame.pack()

    # return a list with credentials Ex: {'user': 'username', 'pass': 'password'}
    def update(self, var1, var2):
        self.mydict = {
                       'username': var1,
                       'password': var2
                       }

    def return_cred(self):
        global mydict
        # Necessary to ensure that the app returns a dictionary type
        self.win.wait_window()
        # stores dict in global variable
        mydict = self.mydict
        return self.mydict

    def submit(self):
        self.update(self.var_1.get(), self.var_2.get())

    # close the window
    def close_win(self):
        self.win.destroy()


# AS A SERIES OF METHOD FOR DEVICE ADMINISTRATION
class CONNECT_TO_DEV:
    def __init__(self, t, entry_frame_1, *entry_frame_2):
        global mydict
        self.command_1 = entry_frame_1
        self.command_2 = entry_frame_2
        self.t = t
        self.username = mydict.get('username')
        self.password = mydict.get('password')
        connection_list = []  # contains ip information such hostname and ip address
        self.new_list = []  # provides variable to run the connection attempt
        for i in self.command_2:
            connection_list.append(i.split('-'))
            for j in connection_list:
                for list_item in j:
                    self.new_list.append(list_item.strip())

    def connect(self):
        try:
            # device connection attributes
            DEV = {
                'device_type': 'cisco_ios',
                'host': self.new_list[1],  # enters device ip address
                'username': self.username,
                'password': self.password
            }
            seperation = '='*20
            dev_connect = ConnectHandler(**DEV)
            output = dev_connect.send_command(self.command_1)

            self.t.insert(

                tkinter.END,
                f'\n\n{seperation}{self.new_list[0]}{seperation}\n\n{output}\n\n'

            )

        except ValueError:
            print('The user entered value different from an ip address')

    def delete_text(self):
        # delete all text within the widget
        self.t.delete(1.0, tkinter.END)

    def configure_device(self):
        try:
            # device connection attributes
            DEV = {
                'device_type': 'cisco_ios',
                'host': self.new_list[1],  # enters device ip address
                'username': self.username,
                'password': self.password
            }
            dev_connect = ConnectHandler(**DEV)
            output = self.t.get(1.0, tkinter.END)

            # save retrieved text from text box
            with open('config_file', 'w') as f:
                f.write(output)

            seperation = '=' * 18
            config_output = dev_connect.send_config_from_file('config_file')

            time.sleep(5)

            self.t.insert(

                tkinter.END,
                f'\n\n{seperation} + {self.new_list[0]} Being Configured + {seperation}\n\n{config_output}\n\n'

            )

        except ValueError:
            print('The user entered value different from an ip address')
