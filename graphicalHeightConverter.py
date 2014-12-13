# This is a program by May
# Update version of height converter because I added graphical user interface
import wx
import math

class HeightConverter(wx.Frame):
	def __init__(self, parent):
		
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Fancy Height Converter")
		self.panel = wx.Panel(self) # Do I have to write self here?
		
		self.feetLabel = wx.StaticText(self.panel, label = "Feet", pos = (40, 10))
		self.inchesLabel = wx.StaticText(self.panel, label = "Inches", pos = (30, 40))
		
		self.feetBox = wx.TextCtrl(self.panel, pos = (75, 10))
		self.inchesBox = wx.TextCtrl(self.panel, pos = (75, 40))
		
		self.BtnEnter = wx.Button(self.panel, label = "Enter", pos = (70, 65))
		self.BtnEnter.Bind(wx.EVT_BUTTON, self.OnConvert)
		
		self.Show()
		
		self.response = wx.StaticText(self.panel, label = " ", pos = (40, 100))
		
	def OnConvert(self, e):
		feet = self.feetBox.GetValue()
		inches = self.inchesBox.GetValue()
		
		try:
			feet = int(feet)
		except:
			wx.MessageBox("Converter requires you to enter a number in feet, I will just say you are 0 feet short", "Random Feet", wx.OK | wx.CANCEL)		
			self.feetBox.SetValue(str(0))  #Set value need to be str for text box
			feet = 0
		
		try:
			inches = int(inches)
		except:
			wx.MessageBox("Converter requires you to enter a number in inches, I will just say you are 0 inches short", "Random Inches", wx.OK | wx.CANCEL)		
			self.inchesBox.SetValue(str(0)) 
			inches = 0
					 
			         
		if inches > 12:
			wx.MessageBox("You should learn how to convert unit! This time I will convert 12" \
			" inches to 1 foot for you!", "Learn Conversion", wx.OK | wx.CANCEL)
			extraFeet = inches / 12
			self.inchesBox.SetValue(str(inches - extraFeet * 12))
			
			inches -= extraFeet * 12
			self.feetBox.SetValue(str(feet + extraFeet))
			feet += extraFeet
            
		Centimeter = 30.48 * feet + 2.54 * inches
		self.response.SetLabel("You are "+ str(Centimeter)+ " tall.")
        
        
# -------Main program------

app = wx.App(False)

frame = HeightConverter(None)
app.MainLoop()
		
		
	