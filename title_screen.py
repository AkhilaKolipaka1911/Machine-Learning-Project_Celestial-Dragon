from tkinter import *
# from tkinter import tkvideo
import tkinter as tk

import time
import sys
from PIL import Image, ImageTk
import os
from itertools import count, cycle

def run():
    os.system('python test.py')


'''WIDTH = 800
HEIGHT = 450
xVelocity = 3
yVelocity = 3
# n=100

window = Tk()
window.title('Crelestial Dragon')

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

# lblVideo = Label(window)
# lblVideo.pack()
# player = tkvideo("video.mp4",
#                  lblVideo,
#                  loop=1,
#                  size=(700,400))
#
background_img = PhotoImage(file="img_4.png")
big_background_img = background_img.zoom(2)
background = canvas.create_image(0,0,image=background_img,anchor=NW)

photo_image = PhotoImage(file='img2.png')
small_photo_image = photo_image.subsample(5)
my_image = canvas.create_image(0,0,image=small_photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

btn = Button(window, text="Click Me", bg="black", fg="white",command=run)
btn.pack()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=WIDTH or coordinates[0]<0):
        xVelocity = xVelocity*(-1)
    if (coordinates[1] >= HEIGHT or coordinates[1] < 0):
        yVelocity = yVelocity * (-1)
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()'''

class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
 
#demo :
root = tk.Tk()
lbl = ImageLabel(root)

l = tk.Label(root, text = "Celestial Dragon", bg='black', fg='white', font=('Comic Sans MS', 25, 'bold'))
lbl.load('C:\\Users\\kolipaka akhila\\Desktop\\ml project\\giff.gif')
btn = Button(root, text="Predict Transportation", bg='black', fg="white",font=('Comic Sans MS', 10, 'bold'), command=run)
btn.place(x=60, y=190)
l.place(x=200)
lbl.pack()
root.mainloop()