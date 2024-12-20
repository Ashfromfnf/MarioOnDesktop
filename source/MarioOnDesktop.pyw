import tkinter as tk
from PIL import Image, ImageTk
from pynput import keyboard
import random

root = tk.Tk()
root.title("😂")

imgResolutionFixed = [519, 481]

SPEED = 50

l = keyboard.Key.left
r = keyboard.Key.right
u = keyboard.Key.up
d = keyboard.Key.down

pos = [0, 0]


def main():
    Image.Resampling.NEAREST
    image = Image.open('image.png')
    image = image.resize((imgResolutionFixed[0], imgResolutionFixed[1]))
    image = ImageTk.PhotoImage(image)

    root.attributes("-transparentcolor", "white")

    root.geometry("{}x{}".format(str(imgResolutionFixed[0]*1), str(imgResolutionFixed[1]*1)))

    root.geometry('+{}+{}'.format(pos[0], pos[1]))

    root.protocol("WM_DELETE_WINDOW", "altf4")



    


    image_label = tk.Label(root, image=image, bg="white")

    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", "white")

    image_label.pack()

    root.mainloop()

def altf4():
    print("nuh uh")

def change_position(root_variable,x,y):
    pos[0] = pos[0] + x
    pos[1] = pos[1] + y
    root.geometry('+{}+{}'.format(pos[0], pos[1]))




def f(key): 
    if key == l:
        change_position(root, 0-SPEED, 0)
    if key == r:
        change_position(root, SPEED, 0)
    if key == u:
        change_position(root, 0, 0-SPEED)       
    if key == d:
        change_position(root, 0, SPEED)      
 
keyboard.Listener(on_press=f).start() 




main()



