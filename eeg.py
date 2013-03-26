import sys, os, gc
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
from matplotlib.figure import Figure
import wx
import numpy as np
import matplotlib.pyplot as mp
import math as m
import scipy.io as sc
import scipy.stats as st
from time import *
from xlwt.Workbook import *
from xlwt.Style import *
from array import *
import wx.lib.sheet as sheet
import wx.lib.plot as plot


currentmatfile = 0



class Eeg_Gui(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title,(-1,-1),wx.Size(600,600))
		
		
		
		menubar= wx.MenuBar()
		self.panel = wx.Panel(self)
		
		
		self.init_plot()
		file = wx.Menu()
		
		load = wx.MenuItem(file,1,'&load')
		file.AppendItem(load)
		self.Bind(wx.EVT_MENU , self.loadmatfile , id = 1)
		
		
		quit = wx.MenuItem(file,2,'&Quit')
		file.AppendItem(quit)
		self.Bind(wx.EVT_MENU , self.OnQuit , id = 2)
		
		menubar.Append(file , '&File')
		

		tools = wx.Menu()
		
		daub = wx.MenuItem(tools,3,'&load')
		tools.AppendItem(daub)
		self.Bind(wx.EVT_MENU , daubtran , id = 3)
		
		menubar.Append(tools , '&Tools')
		
		self.SetMenuBar(menubar)
		self.sb = self.CreateStatusBar()
		self.SetMaxSize((600, 500))
		self.SetMinSize((600, 500))

		
		
	
	

	def OnQuit(self,event):
		self.Close()
		
	def init_plot(self):
		self.dpi = 100
		self.fig = Figure()
		
		self.canvas = FigCanvas(self.panel, -1,self.fig)
		
		self.axes = self.fig.add_subplot(211)
		self.axes.set_axis_bgcolor('black')
		self.axes.set_title('no file loaded', size=12)
		self.axes.plot(np.arange(len(np.linspace(0,13))),np.linspace(0,13))
		self.axes2 = self.fig.add_subplot(212)
		self.axes2.set_axis_bgcolor('black')
		self.axes2.set_title('no file loaded', size=12)
		self.axes2.plot(np.arange(len(np.linspace(0,13))),np.linspace(0,13))
	
		print 'here first'
		
		

	def draw_plot1(self,a):
		self.axes.set_title('matfile loaded', size=12)
		self.axes.plot(a)
		self.canvas.draw()
		print 'canvas redrawn'
		
	def draw_plot2(self,a):
		self.axes2.set_title('matfile loaded', size=12)
		self.axes2.plot(a)
		self.canvas.draw()
		print 'canvas redrawn'
		
		


					
	def loadmatfile(self,event):
		dlg = wx.FileDialog(self,message="Choose a file",wildcard = "*.mat")
		
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			print path + " is loaded"
			mat=sc.loadmat(path)
			a=mat['val'][1]
			print a
			self.draw_plot1(a)
			
			
			
			

		dlg.Destroy()
		
			
def daubtran(event):
	pass
	
def main():
	app=wx.App()
	frame=Eeg_Gui(None,-1,'EEGAnalyser')
	
	frame.Show()
	app.MainLoop()
	
main()
	

