#################################################################################

#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

################################################################################
##global variables
mainDir     = "E:/CrowdB2/input.txt"
dictionary  = {}
################################################################################


def updateInfo(dir):
    fo = open(dir, "r")
    for linea in fo:
        if linea[0] != "#":
            pos = linea.find(":")
            key = linea[:pos]
            val = linea[pos+1:].strip()
            dictionary[key] = val
    fo.close()


def addEntry () :
    phonelist.append ([nameVar.get(), phoneVar.get()])
    setSelect ()

Gtextvars   = []

def createGrid(frame):
    cont = 0
    Label(frame, text="Variables").grid(row=cont, column=0, sticky=W, padx = 10, pady =2)
    Label(frame, text="Values").grid(row=cont, column=3, sticky=W, padx = 10, pady =2)
    cont += 1
    for name in dictionary :
        Label(frame, text=name).grid(row=cont, column=0, sticky=W, padx = 10, pady = 2)
        nameVar = StringVar(value = dictionary[name])
        Gtextvars.append(nameVar)
        entry = Entry(frame, textvariable= nameVar, width=40)
        entry.grid(row=cont, column=3, sticky=W)
        
        Label(frame, text="").grid(row=cont, column=4, sticky=W, padx = 10, pady =2)
        cont    += 1
    #for
    Label(frame, text="").grid(row=cont, column=0, sticky=W, padx = 10, pady =2)
#def createGrid
def makeWindow () :
    global nameVar, select
    win = Tk()
    win.title("YML Generator")
    #win.geometry("500x600")

    frame1 = Frame(win)
    frame1.pack()
    

    createGrid(frame1)


    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    b1 = Button(frame2,text=" Add  ",command=addEntry)
    b2 = Button(frame2,text="Update",command=addEntry)
    
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    
    return win




################################################################################
if __name__ == "__main__":
    updateInfo(mainDir)
    win = makeWindow()
    win.mainloop()
    #top = Tk()
    #Application(top).mainloop()
    

            