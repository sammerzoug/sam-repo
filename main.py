import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from re import *
from connection_to_device import CONNECT_TO_DEV as CONN
from connection_to_device import credential as c
from application_popup import mainWindow as Window
from ip_information import Main_Window


# -------------------------------FRAME 1-----------------------------------------------------
# Create our master object to the Application
root = tk.Tk()
root.title('Network Automation For Labing')  # application title
root.resizable(False, False)
root.geometry('730x500')


# create a frame to insert or text widget
frame_1 = tk.Frame(
            root,
            highlightbackground='dark grey',
            highlightthickness=2
            )

# place the frame within the application window
frame_1.place(
              relx=0.25,
              rely=0.22,
              relwidth=0.75,
              relheight=0.6
              )

# Create the text widget
text_widget = tk.Text(master=frame_1)

# Create a scrollbar
scroll_bar = tk.Scrollbar(
                          master=frame_1,
                          orient='vertical',
                          bg='grey'
                          )

# Pack the scroll bar
# Place it to the right side, using tk.RIGHT
scroll_bar.pack(
                side=RIGHT,
                fill='y'
                )

text_widget.config(
                   yscrollcommand=scroll_bar.set,
                   font=('helvica', 8),
                   background='light grey'
                   )

scroll_bar.config(command=text_widget.yview)

# pack the widget
text_widget.place(
                  anchor='nw',
                  relx=0.015,
                  rely=0.1,
                  relwidth=0.94,
                  relheight=0.8
                  )
# -------------------------------FRAME 2-----------------------------------------------------

# Frame for additional options
frame_2 = tk.Frame(
                   root,
                   highlightbackground='dark grey',
                   highlightthickness=2
                   )

frame_2.place(
              relx=0,
              rely=0.22,
              relwidth=0.25,
              relheight=0.6
              )

# =================COMBOBOX CONFIGURATION======================


# configure devices
def configure():
    command = CONN(
                   text_widget,
                   entry.get(),
                   display_selection()
                   )

    command.configure_device()


# list of items
dev_hostname = []
dev_ip = []


#  clears combobox output so the user can enter new values
def clear_dic():
    combo.delete(0, END)
    combo['value'] = ['Default Value']


# combobox list is captured and returned
def display_selection():
    # Get the selected value.
    selection = combo.get()
    # return selected value
    return selection


text_frame_3 = tk.Text(frame_2,
                       height=1,
                       width=15,
                       background='light grey'
                       )
text_frame_3.place(relx=.48,
                   rely=0.12,
                   anchor=CENTER
                   )

text_frame_3.insert(END,
                    'SELECT DEVICE'
                    )
# prevents the user from modifying the label
text_frame_3.config(state=DISABLED)

"""
  Example of a dictionary
  dev_dict = {
        'customer': '192.168.6.103',
        'core': '192.168.6.102',
        'PE1': '192.168.6.100',
        'PE2': '192.168.6.101',
        'cloud': '192.168.6.99'
    }
    
"""
#  default value in the dropdown menu
value = [
        'No Entries'
    ]

combo = ttk.Combobox(frame_2, width=18, state="readonly", values=value)
combo.place(relx=0.48, rely=0.2, anchor=CENTER)
# my_var = f'You have selected {display_selection(event=NONE)}'
# combo.bind("<<ComboboxSelected>>", my_var)


# enter_dev_hostname() is required to collect user entry for both hostname and ip address
def enter_dev_hostname():
    my_ip_add = []  # stores ip address
    my_host = []  # stores hostname
    combo.delete(0, END)
    my_window = Main_Window(frame_2)
    returned_dev_list = my_window.main()

    # builds a list of value from dict list
    my_list = [j for i in returned_dev_list for j in i.values()]

    # should avoid matching an ip address for ex: 192.168.6.1
    for item in my_list:
        m = search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', f'{item}')
        if m is not None:
            octet = item.split('.')
            if len(octet) == 4:
                var = f'{item}'
                my_ip_add.append(var)

    for item in my_list:
        m = search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', f'{item}')
        if m is None:
            my_host.append(item)

    i = 0
    while i < len(my_ip_add):
        for item in my_host:
            my_ip_add[i] = f'{item} - {my_ip_add[i]}'
            i += 1

    combo['value'] = my_ip_add  # assigned new list to combo


ttk.Button(
           frame_2,
           text='Add',
           width=7,
           command=enter_dev_hostname
           ).place(relx=0.25, rely=0.295, anchor=CENTER)

ttk.Button(
           frame_2,
           text='Clear',
           width=7,
           command=clear_dic
           ).place(relx=0.74, rely=0.295, anchor=CENTER)

ttk.Button(
           frame_2,
           text='Configure',
           command=configure
           ).place(relx=0.48, rely=0.4, anchor=CENTER)

some_dict = {}


def send_cred():
    global some_dict
    cred = c(frame_2)
    some_dict = cred.return_cred().copy()


ttk.Button(
           frame_2,
           text='Credential',
           command=lambda: [send_cred()]
           ).place(relx=0.48, rely=0.6, anchor=CENTER)

lbl = Label(
            frame_2,
            text='CREDENTIAL PROFILE',
            background='green'
            )

lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

# -----------------------------------ROOT-----------------------------------------------------

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("cisco-modeling-labs-enterprise-lp-banner_1.png"))

# Create a Label Widget to display the text or Image
label = Label(root, image=img)
label.place(
     relx=0.0,
     rely=-0.03,
     )

"""
     The below code contains states that this application
     is designed and owned by Sam Merzoug
"""
design_by = label = Label(
                            root,
                            text='@designed by Sam Merzoug',
                            font=('bold', 7)
                         )

design_by.place(
    relx=1,
    rely=1,
    anchor='se'
)

# Root buttons
entry = Entry(
              root,
              width=30
              )

entry.place(
            relx=.5,
            rely=0.88,
            anchor='s'
            )


# will get data and post the output in
# text widget
def get_data():
    command = CONN(
                   text_widget,
                   entry.get(),
                   display_selection()
                   )

    command.connect()


# delete output within text widget
def delete_output():
    command = CONN(
                   text_widget,
                   entry.get(),
                   display_selection(),
                   )

    command.delete_text()


def upload_action():
    win = Window(root)
    win.popup()


# Create a button to get the input data
ttk.Button(
           root,
           text='Show Output',
           command=get_data
           ).place(relx=0.43, rely=0.95, anchor='s')

ttk.Button(
           root,
           text='Del Output',
           command=delete_output
           ).place(
                relx=0.56,
                rely=0.95,
                anchor='s'
                )

ttk.Button(
           root,
           text='See Network Map',
           width=15,
           command=upload_action
           ).place(
            relx=.76,
            rely=0.885,
            anchor='s'
            )

ttk.Button(
           root,
           text='Exit',
           width=10,
           command=root.destroy
           ).place(
            relx=.76,
            rely=0.95,
            anchor='s'
            )


# Start the mainloop
tk.mainloop()
