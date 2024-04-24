import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:
    # Initializing the Notepad application
    __root = Tk()  # Creating the main window
    __thisWidth = 300  # Setting default width
    __thisHeight = 300  # Setting default height
    __thisTextArea = Text(__root)  # Creating a text area widget
    __thisMenuBar = Menu(__root)  # Creating the menu bar
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)  # Creating a File menu
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)  # Creating an Edit menu
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)  # Creating a Help menu
    __thisScrollBar = Scrollbar(__thisTextArea)  # Creating a scrollbar
    __file = None  # File attribute to store current file

    def __init__(self, **kwargs):
        # Setting window properties like icon, width, and height
        try:
            self.__root.wm_iconbitmap("Notepad.ico")  # Setting application icon
        except:
            pass
        
        try:
            self.__thisWidth = kwargs["width"]  # Checking for custom width
        except KeyError:
            pass
        
        try:
            self.__thisHeight = kwargs["height"]  # Checking for custom height
        except KeyError:
            pass
        
        self.__root.title("Untitled - Notepad")  # Setting default title
        
        # Positioning the window in the center of the screen
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)
        self.__root.geometry("%dx%d+%d+%d" % (self.__thisWidth, self.__thisHeight, left, top))
        
        # Configuring grid for responsive layout
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Adding text area to the grid layout
        self.__thisTextArea.grid(sticky=N + E + S + W)

        # File Menu
        self.__thisFileMenu.add_command(label="New", command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open", command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit", command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)

        # Edit Menu
        self.__thisEditMenu.add_command(label="Copy", command=self.__copy)
        self.__thisEditMenu.add_command(label="Cut", command=self.__cut)
        self.__thisEditMenu.add_command(label="Paste", command=self.__paste)
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)

        # Help Menu
        self.__thisHelpMenu.add_command(label="About Notepad", command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)

        # Configuring menu
        self.__root.config(menu=self.__thisMenuBar)

        # Adding scrollbar to the text area
        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
        # Quit the application
        self.__root.destroy()

    def __showAbout(self):
        # Show information about the application
        showinfo("Notepad", "This project was created by Marios-Angelos Platon ")

    def __openFile(self):
        # Open a file and display its content in the text area
        self.__file = askopenfilename(defaultextension=".txt",
                                       filetypes=[("All Files", "*.*"),
                                                  ("Text Documents", "*.txt")])
        if self.__file == "":
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)
            file = open(self.__file, "r")
            self.__thisTextArea.insert(1.0, file.read())
            file.close()

    def __newFile(self):
        # Create a new file
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):
        # Save the content in the text area to a file
        if self.__file is None:
            self.__file = asksaveasfilename(initialfile="Untitled.txt",
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])
            if self.__file == "":
                self.__file = None
            else:
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __copy(self):
        # Copy selected text
        self.__thisTextArea.event_generate("<<Copy>>")

    def __cut(self):
        # Cut selected text
        self.__thisTextArea.event_generate("<<Cut>>")

    def __paste(self):
        # Paste copied or cut text
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):
        # Run the main application loop
        self.__root.mainloop()


notepad = Notepad(width=600, height=400)
notepad.run()
