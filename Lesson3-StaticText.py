#! /usr/bin/env python

#This app will not run because something is missing from line 4. Do you know what it is?
import wx

def GreatClick(e):
	print("Great! Me too!")
def BadClick(e):
	print("Aww.. That is just too bad")
	
app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "This is Lesson 3")
panel = wx.Panel(frame)

#Here is something new. I bet you can figure out what it does.
heading = wx.StaticText(panel, label='This is a StaticText Label', pos = (130, 15))
wx.StaticLine(panel, pos = (100, 60), size = (220, 2))
btnLike = wx.Button(panel, label = "I Like Static Text", pos = (100,30), size = (200,20))
btnLike.Bind(wx.EVT_BUTTON, GreatClick)

# Another heading
Aheading  = wx.StaticText(panel, label = "This is more static text", pos = (130, 60), size = (400,20))
wx.StaticLine(panel, pos = (100, 110), size = (220,2))
btnHate = wx.Button(panel, label = "I don't like static text", pos = (100, 80), size = (200, 20))
btnHate.Bind(wx.EVT_BUTTON, BadClick)

frame.Show()

app.MainLoop()


# ----------- Exercises Below -----------------

#1. Did you figure out what was missing on line 4?
#   HINT: Does python know what a frame is automatically?

#2. Make that button print "Great! Me Too!" to the terminal when it is clicked.
#   Look back at the last lesson if you need to, but please don't copy-paste the code.
#   Typing it yourself will help you remember.

#3. Insert the following code on line 15.
#   wx.StaticLine(panel, pos=(100, 60), size=(220,2))
#   And, of course run the program to see what happened.

#4. Below the horizontal line, add more static text that says "This is more static text"
#   And then add a button that says "I don't like static text"
#   Make the new button print "Aww, too bad" to the terminal.