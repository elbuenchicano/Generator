﻿#################################################################################

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
#mainDir     = "D:/graderia/testmix_hofm/valid.yml"
#mainDir     = "D:/CrowdB2/PruebaSib/ofcm/ofcmvalid.yml"
mainDir     = "D:/subway/prueba2/valid.yml"
#mainDir     = "D:/peds2/prueba/sib6valid.yml"
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
def colectInfo(valu):
    out = ""
    pos = 0
    for name in sorted(dictionary):
        valf = Gentries[pos].get()

        valf = valf.replace("{i}",str(valu))
        out += name + ": " + valf + "\n"   
        pos += 1
    out = out.replace("%YAML: 1.0","%YAML:1.0")
    return out
#def updateinfo
#################################################################################
def save_olds() :
    fo      = open("./saveold", "w")
    fo.write(entry.get())
    #fo.write("\n")
    fo.write(entry3.get())
    fo.close()
#def save_olds


def xfrange(start, stop, step):
    while start < stop:
        yield start
        start += step

################################################################################
def generate() :
    out     = ""
    batOut  = "@echo off\n"
    pos     = 0
    fexe   = entry.get().replace("\n"," ")
    outbat  = entry3.get() + "/" + entry2.get() + ".bat"
    try:
        out_fileb = open(outbat, "w")
        out_fileb.write(batOut)
        
        ini = float( ent_ini.get() )
        fin = float( ent_fin.get() )
        incr = float( ent_incr.get() )
        
        r = xfrange(ini,fin,incr)

        for x in r:
            tok = x*1000
            tok = int(tok)
            outyml  = entry3.get() + "/" + entry4.get() + str(tok) +".yml"
            batOut  = fexe + " " + outyml + "\n"  
            out_fileb.write(batOut)

            out = colectInfo(x)
            out_filey = open(outyml, "w")
            out_filey.write(out)
            out_filey.close()
        out_fileb.close()
        messagebox.showinfo("info", "All Saved")
    except:
        messagebox.showinfo("info", "No Info")   
    save_olds()

#def generate
#################################################################################
def generate_list():
    a = 2
#def generatelist
#################################################################################
def load_olds() :
    fo      = open("./saveold", "r")
    entry.insert(0,fo.readline())
    entry3.insert(0,fo.readline()) 
    fo.close()

#def save_vals
#################################################################################
def createHeader(frame) :

    global entry, entry2, entry3, entry4, ent_ini, ent_fin, ent_incr

    entry = Entry(frame, width=30)
    entry.grid(row = 0, column =0)

    entry2 = Entry(frame, width=10)
    entry2.grid(row = 0, column =2)
    entry2.insert(0,"batOut")

    b1 = Button(frame,text="File .exe",command=load_file, width = 10).grid(row = 0, column =1)
    b2 = Button(frame,text="Generate \nBat",command=generate, width = 10).grid(row = 0, column =3, rowspan = 2, sticky='ns')
    
    entry3 = Entry(frame, width=30)
    entry3.grid(row = 1, column =0)
    
    entry4 = Entry(frame, width=10)
    entry4.grid(row = 1, column =2)
    entry4.insert(0,"test")

    b3 = Button(frame,text="Dir store",command=load_file2, width = 10).grid(row = 1, column =1)
    #return 

    Label(frame, text="Ini - Incr - Fin : {i}").grid(row=3, column=0, sticky=W, padx = 10, pady =2)
    ent_ini = Entry(frame, width=10)
    ent_ini.grid(row = 3, column =1)
    ent_incr = Entry(frame, width=10)
    ent_incr.grid(row = 3, column =2)
    ent_fin = Entry(frame, width=10)
    ent_fin.grid(row = 3, column =3)

    ent_ini.insert(0,"1")
    ent_incr.insert(0,"1")
    ent_fin.insert(0,"1")

    b4 = Button(frame,text="Generate \nList",command=generate_list, width = 10).grid(row = 0, column =4, rowspan = 2, sticky='ns')

    load_olds()
    
    

def createGrid(frame):
    
    createHeader(frame)   

    #-----------------------------------------------------------------------------
    #cont = 4
    
    #Label(frame, text="").grid(row=cont, column=0, sticky=W, padx = 10, pady =2)
    #Label(frame, text="").grid(row=cont, column=1, sticky=W, padx = 10, pady =2)
    
    cont = 5

    Label(frame, text="Variables").grid(row=cont, column=0, sticky=W, padx = 10, pady =2)
    Label(frame, text="Values").grid(row=cont, column=1, sticky=W, padx = 10, pady =2)
    cont += 1
    for name in sorted(dictionary) :
        Label(frame, text=name).grid(row=cont, column=0, sticky=W, padx = 10, pady = 2)
        nameVar = StringVar(value = dictionary[name])
        Gtextvars.append(nameVar)
        entryg = Entry(frame, textvariable= nameVar, width=35)
        entryg.grid(row=cont, column=1, sticky=W, columnspan = 3)
        Gentries.append(entryg)
        #Label(frame, text="").grid(row=cont, column=6, sticky=W, padx = 1, pady =3)
        cont    += 1
    #for
    Label(frame, text="").grid(row=cont, column=0, sticky=W, padx = 10, pady =2)


################################################################################
def load_file():
    fname = tkFileDialog.askopenfilename()
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
# http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame

class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar  = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas      = Canvas(self, bd=0, highlightthickness=0,
                             yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)
        canvas.config(width=200,height=700)
        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)

######################################################################################
######################################################################################
######################################################################################
if __name__ == "__main__":

    class SampleApp(Tk): 
        def __init__(self, *args, **kwargs):
            root = Tk.__init__(self, *args, **kwargs)
            self.frame = VerticalScrolledFrame(root)
            self.frame.pack()
            self.label = Label(text="Yml generator", font=("Helvetica", 8), anchor = E)
            self.label.pack()
            createGrid(self.frame.interior)
    #................................................................................
    updateInfo(mainDir)
    app = SampleApp()
    app.mainloop()   
            