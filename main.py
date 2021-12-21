from tkinter import *
from tkinter import filedialog
from shutil import copytree


def checker():
    if (source != None) and (destination != None):
        Button(root, justify="center", text="Begin Copying", command=lambda: copytree(source, destination, dirs_exist_ok=True)).place(bordermode="outside", anchor="center", x=400, y=300)


def getDirectories(location):
    global source
    global destination
    if location == "source":
        source = filedialog.askdirectory()
        Label(root, text=source).place(bordermode="outside", anchor="center", x=400, y=100)
    if location == "destination":
        destination = filedialog.askdirectory()
        Label(root, text=destination).place(bordermode="outside", anchor="center", x=400, y=200)
    checker()


source = None
destination = None
root = Tk()
root.title("Simple Backup")
root.geometry("800x600")

Button(root, justify="center", text="Choose Source Directory", command=lambda: getDirectories("source")).place(bordermode="outside", anchor="center", x=400, y=50)
Button(root, justify="center", text="Choose Destination Directory", command=lambda: getDirectories("destination")).place(bordermode="outside", anchor="center", x=400, y=150)

root.mainloop()
