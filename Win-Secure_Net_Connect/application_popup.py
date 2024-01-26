from tkinter import *
from PIL import ImageTk, Image
from tkinter import font as tkFont
from tkinter import filedialog as fd


# This popup window configuration
class popupWindow(object):
    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('Network Topology')
        top.geometry('400x300')
        self.helv36 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD)
        self.btn_1 = Button(top, width=20, text='Show Network Map', font=self.helv36, command=self.show_map)
        self.btn_1.place(relx=.35, rely=0.15, anchor=CENTER)
        self.btn_2 = Button(top, font=self.helv36, text='Close', command=self.cleanup)
        self.btn_2.place(relx=.69, rely=0.15, anchor=CENTER)

    def show_map(self):
        """
         - Import "tkinter" as "tk" and "filedialog" for creating the GUI components and opening the
         folder dialog. We also import PIL (Pillow) to work with images.
         - Define the "open_image()" function, which opens the file dialog using
         "filedialog.askopenfilename()". This dialog allows the user to select an image file with
         specified file types (PNG, JPG, JPEG, GIF, BMP, ICO). If a file is selected, it calls the
         "display_image()" function.
         - Define the "display_image()" function, which opens the selected image file using Pillow
         (Image.open()) and displays it in a Tkinter label widget. The ImageTk.PhotoImage class
         converts the image into a format that can be displayed in Tkinter. The status label shows the
         loaded image path
         """

        # file type
        filetypes = (
            ('image files', '*.png'),
            ('All files', '*.*')
        )
        # show the open file dialog
        f = fd.askopenfile(
                    mode='rb',
                    filetypes=filetypes
                    )
        image = Image.open(f)
        photo = ImageTk.PhotoImage(image)

        # Create a Label Widget to display the text or Image
        label = Label(
                self.top,
                image=photo
                )
        label.photo = photo

        label.place(
            relx=0.075,
            rely=0.2
        )

    def cleanup(self):
        self.top.destroy()


class mainWindow(object):
    def __init__(self, master):
        self.w = None
        self.master = master

    def popup(self):
        self.w = popupWindow(self.master)
