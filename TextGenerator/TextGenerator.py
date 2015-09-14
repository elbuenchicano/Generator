#################################################################################

#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
from tkinter.filedialog import askopenfilename

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
    
    import tkinter.filedialog as tkFileDialog
    import tkinter.simpledialog as tkSimpleDialog    #askstring()

################################################################################
##global variables
fname       = ""
dictionary  = {}
################################################################################

global win
Gtextvars   = []
Gentries    = []
Gtextvars   = []


################################################################################

def load_file():
    fname = tkFileDialog.askdirectory()
    if fname:
        try:
            print(fname)
            entry.delete(0,END)
            entry.insert(0,fname)
        except:                     # <- naked except is a bad idea
            showerror("Open Source File", "Failed to read file\n'%s'" % fname)
#def load_file
################################################################################
def updateInfo(dir):

    if dir != "":
        fo      = open(dir, "r")
        for linea in fo:
            if linea[0] != "#":
                pos = linea.find(":")
                key = linea[:pos]
                val = linea[pos+1:].strip()
                dictionary[key] = val
        fo.close()
#def updateinfo
################################################################################
def addEntry () :
    tkFileDialog.askopenfile(mode='r', **self.file_opt)


#def addentry
################################################################################
def createGrid(frame):
    cont = 0
    Label(frame, text="Variables").grid(row=cont, column=0, sticky=W, padx = 10, pady =2)
    Label(frame, text="Values").grid(row=cont, column=2, sticky=W, padx = 10, pady =2)
    cont += 1
    for name in dictionary :
        Label(frame, text=name).grid(row=cont, column=0, sticky=W, padx = 10, pady = 2)
        nameVar = StringVar(value = dictionary[name])
        Gtextvars.append(nameVar)
        entry = Entry(frame, textvariable= nameVar, width=60)
        entry.grid(row=cont, column=2, sticky=W)
        Gentries.append(entry)

        Label(frame, text="").grid(row=cont, column=3, sticky=W, padx = 5, pady =2)
        cont    += 1
    #for
    Label(frame, text="").grid(row=cont, column=0, sticky=W, padx = 10, pady =2)
#def createGrid

################################################################################
def makeWindow () :
    global entry,entry2
    win = Tk()
    win.title("YML Generator")
 
    frame1 = Frame(win)
    frame1.pack()
    createGrid(frame1)
    
    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    entry = Entry(frame2, width=40)
    entry2 = Entry(frame2, width=20)
    b1 = Button(frame2,text="Browse",command=load_file, width = 10)
    b2 = Button(frame2,text="Update",command=addEntry, width = 20)
    entry.pack(side=LEFT)   
    entry2.pack(side=LEFT)
    b1.pack(side=LEFT)
    b2.pack(side=LEFT)
    
    return win
################################################################################
if __name__ == "__main__":
    updateInfo("E:/CrowdB2/input.yml")
    win = makeWindow()
    win.mainloop()
    
    

            