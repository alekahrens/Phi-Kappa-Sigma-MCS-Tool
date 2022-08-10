import matplotlib.pyplot as plt
import tkinter
import tkinter as tk
from tkinter import *
import pandas as pd

def q1(root,chapter,file):
    chapters = pd.read_excel(file, sheet_name='Foundational', )
    print(chapters)
    q1Label = Label(root, text='Quarter 1:')
    q1Label.place(x=20, y=30)

    q1Count = 0
    q1Total = 6

    #Start of requirements for Quarter 1
    chapterInfo = chapters.loc[chapter,:]
    print(chapterInfo)
    chaptBylaw = Label(root, text='Chapter By-laws')
    chaptBylaw.place(x=20, y=50)
def q2(chapter, file):
    chapters = pd.read_excel(file, sheet_name='Foundational', usecols="A", )

def q3(chapter, file):
    chapters = pd.read_excel(file, sheet_name='Foundational', usecols="A", )

def q4(chapter, file):
    chapters = pd.read_excel(file, sheet_name='Foundational', usecols="A", )

def chapterPerformance(chapter,file, root):
    quarter1 = q1(root, chapter,file)
    #quarter2 = q2(root, chapter,file)
    #quarter3 = q3(root, chapter,file)
    #quarter4 = q4(root, chapter,file)
    #if(quarter1 and quarter2 and quarter3 and quarter4 == True):
        #excellence = Button(root, text='Chapter Excellence', fg='blue')
        #excellence.place(x=200, y=250)


