#################################################################################

#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
from tkinter.filedialog import askopenfilename
from _ast import operator
from tkinter.messagebox import *

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
#fname       = ""
dictionary  = {}
global win
mainDir     = "E:/CrowdB2/input.yml"
execName    = "Base2.exe"
textvars    = []
Gentries    = []
Gtextvars   = []

################################################################################
def updateInfo(dir):
    if dir != "":
        fo      = open(dir, "r")
        for linea in fo:
            if linea[0] != "#" and linea[0] != "\n":
                pos = linea.find(":")
                key = linea[:pos]
                val = linea[pos+1:].strip()
                dictionary[key] = val
        fo.close()

################################################################################
def colectInfo(key , valu):
    out = ""
    pos = 0
    for name in sorted(dictionary):
        valf = Gentries[pos].get()
        if name == key:
            valf = str(valu)
        out += name + ": " + valf + "\n"   
        pos += 1
    return out
#def updateinfo
################################################################################
def addEntry () :
    pos = 0
    out = ""
    batOut = "@echo off\n"
    bounds = []
    key = ""
    for name in sorted(dictionary):
        val = Gentries[pos].get()
        if val[0] == "\"":
            out += name + ": " + val + "\n"
        else:
            if val.find(":") > 0:
                bounds  = val.split(":") 
                key     = name
                break 
            else:
                out += name + ": " + val + "\n"    
        pos += 1

    outbat  = entry.get() + "/" + entry2.get() + ".bat"

    if len(bounds) > 0:
        try:
            out_fileb = open(outbat, "w")
            out_fileb.write(batOut)
            for x in range(int(bounds[0]),int(bounds[2])+1,int(bounds[1])):
                outyml  = entry3.get() + "/" + entry4.get() + str(x) +".yml"
                batOut  = execName + " " + outyml + "\n"  
                out_fileb.write(batOut)

                out = colectInfo(key,x)
                out_filey = open(outyml, "w")
                out_filey.write(out)
                out_filey.close()
            out_fileb.close()
            messagebox.showinfo("info", "All Saved")
        except:
            messagebox.showinfo("info", "No Info")   
    else:
        try:
            outyml  = entry3.get() + "/" + entry4.get() + ".yml"
            batOut  += execName + " " + outyml   
            out_filey = open(outyml, "w") 
            out_filey.write(out)
            out_fileb = open(outbat, "w")
            out_fileb.write(batOut)
            out_fileb.close()
            out_filey.close()
            messagebox.showinfo("info", "Saved")
        except:
            messagebox.showinfo("info", "No Info")
#def addentry
################################################################################
def createGrid(frame):
    cont = 0
    Label(frame, text="Variables").grid(row=cont, column=0, sticky=W, padx = 10, pady =2)
    Label(frame, text="Values").grid(row=cont, column=2, sticky=W, padx = 10, pady =2)
    cont += 1
    for name in sorted(dictionary) :
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

def createSecondGrid(frame):
    global entry, entry2, entry3, entry4
    entry = Entry(frame, width=40)
    entry.grid(row = 0, column =0)
    entry2 = Entry(frame, width=20)
    entry2.grid(row = 0, column =1)
    b1 = Button(frame,text="Dir .bat",command=load_file, width = 10).grid(row = 0, column =2)
    b2 = Button(frame,text="Generate",command=addEntry, width = 20).grid(row = 0, column =3, rowspan = 2, sticky='ns')
    entry3 = Entry(frame, width=40)
    entry3.grid(row = 1, column =0)
    entry4 = Entry(frame, width=20)
    entry4.grid(row = 1, column =1)
    b3 = Button(frame,text="Dir store",command=load_file2, width = 10).grid(row = 1, column =2)

################################################################################
def makeWindow () :
    
    win = Tk()
    win.title("YML Generator")
    frame1 = Frame(win)
    frame1.pack()
    createGrid(frame1)
    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    createSecondGrid(frame2)
 
    return win
#def makewindow
################################################################################
def load_file():
    fname = tkFileDialog.askdirectory()
    if fname !="":
        #try:
        print(fname)
        entry.delete(0,END)
        entry.insert(0,fname)
        #except:                     # <- naked except is a bad idea
        #showerror("Open Source File", "Failed to read file\n'%s'" % fname)
    return fname
################################################################################
def load_file2():
    fname = tkFileDialog.askdirectory()
    if fname !="":
        #try:
        print(fname)
        entry3.delete(0,END)
        entry3.insert(0,fname)
        #except:                     # <- naked except is a bad idea
        #showerror("Open Source File", "Failed to read file\n'%s'" % fname)
    return fname
################################################################################
if __name__ == "__main__":
    updateInfo(mainDir)
    win = makeWindow()
    win.mainloop()
    
    

            