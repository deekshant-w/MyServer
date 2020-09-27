import tkinter as tk
from tkinter import ttk
from tkinter import font  as tkfont
from tkinter import filedialog, messagebox
import json
import os

def mode2_controller(controller):
    controller.show_frame("Mode2")

def folderName(lbl):
    global PROJECT_DIRECTORY
    PROJECT_DIRECTORY = filedialog.askdirectory()
    if(PROJECT_DIRECTORY):
        lbl.configure(text=PROJECT_DIRECTORY)
        lbl.grid(row=3, column=0, padx=60, columnspan=2)

def startServer(projName,err):
    if(PROJECT_DIRECTORY):
        if(not projName.get()):
            projName = 'MyServer'
        else:
            projName = projName.get()

        data = {
            'projectName':projName,
            'projectDir':PROJECT_DIRECTORY
        }

        with open('config.dk','w') as handle:
            handle.write(json.dumps(data))

        os.system('start cmd /k python manage.py runserver')
        os.system('start cmd /k ngrok http 127.0.0.1:8000')
        quit()
    else:
        err.grid(row=3, column=0, padx=60, columnspan=2)
        err.configure(text='Please Select Data Directory')

    

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0,0)
        self.title_font = tkfont.Font(family='Verdana', size=25, underline=1)
        self.buttonFont = tkfont.Font(size=15)
        self.settingsFont = tkfont.Font(family='Verdana', size=15)
        container = tk.Frame(self)
        container.grid(row=0, column=0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage,):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

PROJECT_DIRECTORY = None
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="MyServer", font=controller.title_font)
        label.grid(row=0, column=0, padx=60,pady=(10,25), columnspan=2)
        
        projName = ttk.Label(self, text="Server Name:", font=controller.settingsFont)
        projName.grid(row=1, column=0, padx=(50,0),pady=30)
        
        style = ttk.Style() 
        style.configure('Main.TEntry', foreground = 'blue')
        
        projNameEntry = ttk.Entry(self, justify = tk.CENTER, style='Main.TEntry', font=('Verdana', 10))
        projNameEntry.grid(row=1, column=1, padx=(0,50),pady=30,ipadx=5,ipady=5)
        
        dirLabel = tk.Label(self, text="", font=('Verdana', 10))
        fileDirectory = tk.Button(self, text='Data Directory', font=controller.buttonFont, padx=5, pady=2, command=lambda:folderName(dirLabel))
        fileDirectory.grid(row=2, column=0, padx=50,pady=(30,10), columnspan=2)
       
        server = tk.Button(self, text='Start Server', font=controller.buttonFont, padx=5, pady=2, command=lambda:startServer(projNameEntry,dirLabel))
        server.grid(row=4, column=0, padx=50,pady=60, columnspan=2)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

