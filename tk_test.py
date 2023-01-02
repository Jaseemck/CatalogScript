from tkinter import *
import pandas as pd
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
#from Widget import *
import os
import sys

base_path = getattr(sys, '_MEIPASS','.')+'/'

window=Tk()
# add widgets here

window.title('Catalog2Script')
window.geometry("800x450")
window.resizable(0, 0)
window.iconbitmap(base_path+"icon.ico")

# Dynamic Components
fldr = StringVar()
fl = StringVar()
fldr_str = 'Select workbook directory'
fl_str = 'C:/Qsight/Extract.xlsx'
fldr.set(fldr_str)
fl.set(fl_str)
logfile = StringVar()
logfile_str = 'C:/Qsight/Logs.log'
logfile.set(logfile_str)
finish = 1
directory = os.path.dirname(fl_str)
if not os.path.exists(directory):
    os.makedirs(directory)

dynamic_cmpnts = []



# Banner Background
background_image=PhotoImage(file = base_path+"background2.png")
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def tableau():
    tx1 = Entry(window, textvariable=fldr, fg='black', width=30)    
    tx1.place(x=170, y=300, width=380, height=30)
    dynamic_cmpnts.append(tx1)
    btn1 = Button(window, text='Browse', command=browse, cursor="hand2")
    btn1.place(x=570, y=300, width=100, height=30)
    dynamic_cmpnts.append(btn1)  
    btn3 = Button(window, text='Analyze', command=process, cursor="hand2")
    btn3.place(x=370, y=350, width=100, height=30)
    dynamic_cmpnts.append(btn3)
      

def browse():
    folder = filedialog.askdirectory()
    fldr.set(folder)

def process():
    print("done!!") 

def coming_soon(msg):
    if len(dynamic_cmpnts)>0:
        for cmpnts in dynamic_cmpnts:
            cmpnts.destroy()
    fldr.set(fldr_str)
    fl.set(fl_str)    
    messagebox.showinfo( msg, "This feature will be available with next release")


def on_close():
    dynamic_cmpnts.pop().destroy()
    dynamic_cmpnts.pop().destroy()
    dynamic_cmpnts.pop().destroy()
    window.deiconify() 
       

# taking image from the directory and storing the source in a variable

twb_icon = PhotoImage(file = base_path+"Img/tableau.png")
pbi_icon = PhotoImage(file = base_path+"Img/pbi.png")
qlk_icon = PhotoImage(file = base_path+"Img/qlik.png")
# displaying the picture using a 'Label' by passing the 'picture' variriable to 'image' parameter
'''
t_label = Button(window, image = twb_icon, command=tableau, cursor="hand2")
p_label = Button(window, image = pbi_icon, command=lambda: coming_soon('Qsight-PowerBI'), cursor="hand2")
q_label = Button(window, image = qlk_icon, command=lambda: coming_soon('Qsight-Qlik'), cursor="hand2")
t_label.place(x=170, y=170, width=105, height=105)
p_label.place(x=370, y=170, width=105, height=105)
q_label.place(x=570, y=170, width=105, height=105)
'''
t_label = Button(window, image = twb_icon, command=tableau, cursor="hand2")
t_label.place(x=370, y=170, width=105, height=105)

try:
    window.mainloop()
except Exception as e:
    print("An Error occured while running the Qsight script")
    raise SystemExit
    exit

window.mainloop()