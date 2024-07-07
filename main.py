import time
from tkinter import *

WIDTH = 1200
HEIGHT = 1000
xVelocity = 1
yVelocity = 1
window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background_photo = PhotoImage(file='space2.png')
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

photo_image = PhotoImage(file='Alien2.png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)


image_width = photo_image.width()
image_height= photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=WIDTH-image_width or coordinates[0]<0):
        xVelocity = -xVelocity
    canvas.move(my_image,xVelocity,0)
    window.update()
    time.sleep(0.00)


window.mainloop()