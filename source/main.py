import pyautogui
import time
from tkinter import *
from PIL import Image, ImageDraw
from tkinter import messagebox, filedialog, ttk
import os

writeText = False
def spam():
    if ((len(textEntry.get()) != 0) or (fPath.get() != '')):  # Check if any of the inputs method is filled
        window.lower()
        time.sleep(5)
        if (writeText): #If have any text in the write input, spam it
            pyautogui.write(textEntry.get())
            pyautogui.hotkey('enter')
        else: #Else, open the file and spam it
            f = open(fPath.get(), "r")
            for line in f:
                pyautogui.write(line)
                pyautogui.hotkey('enter')
        window.update_idletasks()
    else:
        messagebox.showinfo(
            title="Error!",
            message="Please choose a file or type a text."
        )


def open_text_file():
    global writeText #Set the var writeText global
    writeText = False #Set the writeText false to spam the file when press the button
    filetypes = (
        ('Text files', '*.txt'),
    )
    # show the open file dialog
    f = filedialog.askopenfile(filetypes=filetypes)
    fPath.set(f.name) #Set the fPath to open the file later in spam
    name = os.path.basename(f.name)
    status.set(f"Status: {name}") #Update status
    window.update_idletasks()


def open_instructions():
    messagebox.showinfo(
        title="Instructions!",
        message=
        """
            First, choose a file or type a text.\n
            After that, press the spam button and wait 5 seconds.\n
            The status bar shows what will be written.
        """
    )

def checkText(var):
    global writeText #Set the var writeText global
    if(var.get() == ''): #If the text input is empty
        writeText = False #Set writeText false
        fPath.set('') #Reset the file path
        status.set("Status: No file/text.") #Reset status
    else:
        writeText = True #Set writeText true to spam the text input
        status.set(f"Status: {var.get()}") #Update status

window = Tk() #Create the program window
window.title("Macro")
window.resizable(False, False)
window.config(padx=10, pady=50)

fPath = StringVar() #Create fPath to store the file path
fPath.set('')

status = StringVar() #Status var text
status.set("Status: No file/text.")

statusLabel = ttk.Label(textvariable=status) #Create the status label
statusLabel.grid(row=1, column=1, columnspan=1)

macroLabel = ttk.Label(text="Macro") #Create the marco input label
macroLabel.grid(row=2, column=0)

var = StringVar()
var.trace("w", lambda name, index,mode, var=var: checkText(var)) #Call the function checkText when the user type something in the input
textEntry = ttk.Entry(
    width=36,
    textvariable=var
)
textEntry.grid(row=2, column=1, columnspan=2)

open_button = ttk.Button( #Create the open file button
    text='Open a File',
    width=36,
    command=open_text_file,
)
open_button.grid(row=3, column=1, columnspan=2)

buttonSpam = ttk.Button( #Create the spam button
    text="Spam",
    width=36,
    command=spam
)
buttonSpam.grid(row=4, column=1, columnspan=2)

buttonInstructions = ttk.Button( #Create the instructions button
    text="Instructions",
    width=36,
    command=open_instructions
)
buttonInstructions.grid(row=5, column=1, columnspan=2)

window.mainloop()
