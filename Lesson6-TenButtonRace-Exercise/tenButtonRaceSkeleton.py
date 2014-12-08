#! /usr/bin/evn python

# Import modules
import wx
import time
import random


# Create TenButtonFrame class
class TenButtonFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Ten Button race")
		self.panel = wx.Panel(self)
		self.BtnStart = wx.Button(self.panel, label = "Start", pos = (150, 200))
		self.BtnStart.Bind(wx.EVT_BUTTON, self.OnStart)
		
		self.buttons = []
		for i in range(10):
			a = random.randint(0, 275)
			b = random.randint(0, 190)
			self.buttons.append(wx.Button(self.panel, label = "Button" + str(i+1), pos = (a, b)))
			
			# When the user clicks the start button, the start button disappears and a new button 
			self.buttons[i].Show(False)
			
			# Bind all the buttons to their event handlers
			self.buttons[i].Bind(wx.EVT_BUTTON, self.OnAnyButton)

		
		
		
		
		
	# Event handler for the start button
	def OnStart(self, e):
		#Make the start button disappear
		self.BtnStart.Show(False)
		self.buttons[0].Show(True)
		self.startTime = time.time()
		
		#Make Button One appear
	def OnAnyButton(self, e):
		clickedButton = e.GetEventObject() # This is the most essential line 
		clickedIndex = self.buttons.index(clickedButton)
		self.buttons[clickedIndex].Show(False)
		
		# When clickedIndex is 9 it will be out of the range(10)
		if clickedIndex == 9:
			self.endTime = time.time()
			timeInterval = self.endTime - self.startTime
			
		# Above steps are for calculating the time interval that take the person to finish clicking all 10 buttons
			self.ending = wx.StaticText(self.panel, label = \
			"Great job! It took you " + str(timeInterval) + " s to complete this game!", pos = (6, 200))
			
		else:
			self.buttons[clickedIndex + 1].Show(True)

	
# -------- Main Program Below ------------
app = wx.App(False)
frame = TenButtonFrame(None)
frame.Show()
app.MainLoop()