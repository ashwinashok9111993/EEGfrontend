import numpy as np
import matplotlib.pyplot as mp
import math as m
import scipy.io as sc
import scipy.stats as st
from time import *
from xlwt.Workbook import *
from xlwt.Style import *
from array import *
from Tkinter import *
from ttk import Frame, Label, Scale, Style



class GUI(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.initUI()

    def loadmat(self):
        print 'ok'
        
    def onExit(self):
		self.quit()

    def initUI(self):
		self.parent.title("EEGanalyser")
		menubar=Menu(self.parent)
		self.parent.config(menu=menubar)
		fileMenu = Menu(menubar)
		fileMenu.add_command(label="load .mat",command = self.loadmat)
		fileMenu.add_command(label="Exit", command=self.onExit)
		menubar.add_cascade(label="File", menu=fileMenu)
		toolsMenu = Menu(menubar)
		toolsMenu.add_command(label="daubechev",command = self.loadmat)
		toolsMenu.add_command(label="plot2pdf", command=self.onExit)
		menubar.add_cascade(label="tools", menu=toolsMenu)
			
       
def main():
    root = Tk() 
    app=GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    

