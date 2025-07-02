
import tkinter as tk
from PIL import Image , ImageTk
import random
window = tk.Tk()
window.geometry("500x360")
window.title("dice roll")

dice = ["C:/Users/shree/jarvis/dice/1.png.png","C:/Users/shree/jarvis/dice/2.png.png","C:/Users/shree/jarvis/dice/3.png.png","C:/Users/shree/jarvis/dice/4.png.png","C:/Users/shree/jarvis/dice/5.png.png","C:/Users/shree/jarvis/dice/6.png.png"]

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image = image1
label2.image = image2

label1.place(x = 40 , y = 100)
label2.place(x = 1000 , y = 100)
def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image = image2)
    label2.image = image2

button = tk.Button(window,text="roll",bg = "white",fg="black",font = "Times 20 bold",  command=dice_roll )
button.place(x=750 , y = 0)

window.mainloop()