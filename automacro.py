from pynput.mouse import Controller, Listener, Button
from tkinter import *
import pyautogui as pag

class Main:

	def __init__(self):

		self.main = Tk()

		self.mainFrame = Frame(self.root)
		self.forLabel = Frame(self.root)

		self.root.title("Automacro")

		self.label= Label(self.mainFrame,text="Close sofware ini untuk disable",bg='yellow',fg='red').pack(side=TOP)
		self.btn = Button(self.mainFrame,text="Tekan ini untuk mengaktifkan",command=self.clicking).pack()

		self.mainFrame.pack()
		self.main.geometry("200x200")

		self.main.mainloop()

	def on_click(self,x, y, button, pressed):
	    if pressed:
	    	pag.press('3')
	    	pag.press('1')


	def clicking(self):
		with Listener(on_click=self.on_click) as listener:
			listener.join()

Main()
