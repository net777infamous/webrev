# Import the required libraries
from tkinter import *
import webview

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

#Make window frameless
win.overrideredirect(True)

# Create a GUI window to view the HTML content


webview.create_window('winone', url='E:/py/vidjs.html', html='', on_top=True, js_api=None, width=530, height=360, background_color='#FFC0CB', frameless=True, easy_drag=True, x= 3080, y=725, transparent=False) 
webview.start()

    