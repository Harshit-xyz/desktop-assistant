from tkinter import * #pip install tkinter
from PIL import Image,ImageTk,ImageSequence #pip install Pillow
import time
import pygame  #pip install pygame
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1980x1080")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("C:\\Users\\DELL\\OneDrive\\Desktop\\books\\iron-man-suit-up-4u1bp2145mj8cexs.webp")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("C:\\Users\\DELL\\Downloads\\avengers_ringtone.mp3")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1980,1080))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.01)
    root.destroy()

play_gif()
root.mainloop()