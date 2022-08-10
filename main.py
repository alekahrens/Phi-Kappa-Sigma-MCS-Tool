import tkinter
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename as file
import chapterDetails as selection
import pandas as pd
import openpyxl
from tkinter.ttk import Combobox
import seal
import chapterDetails as results
def chapterInfo(root,file):
    chapter = cb.get()
    data = pd.read_excel(file, sheet_name='Foundational', usecols="A", )
    chapter = chapter[2:-2]
    clear_frame()
    root.geometry('1000x500')
    root.title('Details on ' + chapter + ' Chapter')
    seal.seal(chapter,root)
    results.chapterPerformance(index, file, root)

def chapterSelection(root, file):
    global chapters
    chapters = pd.read_excel(file, sheet_name='Foundational', usecols="A", )
    list = chapters.values
    list = list[1:]
    clear_frame()
    frameHomeChap = Frame(root, height=350)
    frameHomeChap.pack(side=TOP, fill=X)
    root.geometry('500x350')
    root.title('Phi Kappa Sigma MCS')

    openImg = Image.open("../PKS_Chapter_Health_Tool/PKS.png")
    importImg = ImageTk.PhotoImage(openImg)
    img = tkinter.Label(image=importImg)
    img.image = importImg
    img.place(x=175, y=0)

    global cb

    cb = Combobox(root, values=list, width=30, state='readonly')
    cb.place(x=150, y=200)

    back = Button(root, text='Back', fg='blue', command=lambda: home(root))
    back.place(x=200, y=250)

    submit = Button(root, text="Submit", fg='blue', command=lambda: chapterInfo(root,file))
    submit.place(x=265, y=250)


def home(root):
    clear_frame()
    frameHome = Frame(root, height=350)
    frameHome.pack(side=TOP, fill=X)
    root.geometry('500x350')
    root.title('Phi Kappa Sigma MCS')
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file="../PKS_Chapter_Health_Tool/pks-grand-chapter-seal.png"))

    openImg = Image.open("../PKS_Chapter_Health_Tool/PKS.png")
    importImg = ImageTk.PhotoImage(openImg)
    img = tkinter.Label(image=importImg)
    img.image = importImg
    img.place(x=175, y=0)

    chaptSearch = Button(root, text='Chapter Search', fg='blue', command=lambda:chapterSelection(root, filename))
    chaptSearch.place(x=90, y=250)


    chaptAwards = Button(root, text='Chapters Awards', fg='blue')
    chaptAwards.place(x=320, y=250)

    bio = Label(text='Created by Alek Ahrens of the Beta Chi Chapter Fall 2020')
    bio.place(x=100,y=320)
def data():
    global filename
    filename = file()

def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False,False)
    data()
    home(root)
    root.mainloop()