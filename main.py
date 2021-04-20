#!/usr/bin/env python3

from yeelight import Bulb
from tkinter import *

root = Tk()

bulb = Bulb("192.168.0.105", auto_on=True)
bulb.effect = "smooth"

class yee:
    def tog():
        bulb.toggle()
    def acender():
        bulb.turn_on()
    def apagar():
        bulb.turn_off()
    def rgb(r,g,b):             # R,G,B:0-255
        bulb.set_rgb(r,g,b)
    def hsv(h,s,v):             # Hue:0-359   Saturacao:0-100   Value:0-100   H=rgb  V=brightness
        bulb.set_hsv(h,s,v)
    def brightness(n):          # N:0-100
        bulb.set_brightness(n)
    def temperatura(t):         # T: 1000-10000
        bulb.set_color_temp(t)
    def setdefault():           #????
        bulb.set_default()

# thread = threading.Thread(target=bulb.listen, args=(callback,))
# thread.start()

###TKINTER###

#create a widget
myLabel = Label(root, text="teste")

toggle = Button(root, text="toggle", command=lambda: yee.tog())
red = Button(root, text="red", command=lambda: yee.rgb(255,0,0))
blue = Button(root, text="blue", command=lambda: yee.rgb(0,0,255))
white = Button(root, text="white", command=lambda: yee.temperatura(10000))

#shoving it onto the sceen

toggle.grid(row=1, column=0)
red.grid(row=1, column=1)
blue.grid(row=1, column=2)
white.grid(row=1, column=3)

#rgb_img = ImageTk.PhotoImage(Image.open(""))

#event loop
root.mainloop()
#print(bulb.get_properties())
