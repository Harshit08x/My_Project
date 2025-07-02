from tkinter import*
import tkinter as tk 
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import location
root = Tk()
root.title("Weather App ")
root.geometry("900x500+300+200")
root.resizable("False","False")

def getweather():
    city = textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj .timezone_at(lng=location.longitude,lat=location.latitude)
    
    home = pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text = current_time)
    name.config(text= "CURRENT WEATHER")
   

#searchbox
search_image =PhotoImage(file = "C:/Users/shree/OneDrive/Pictures/Screenshots/search.png.png")
myimage=Label(image=search_image)
myimage.place(x = 20,y=20)

textfield=tk.Entry(root,justify="center",width = 17,font =("poppins",25,"bold"),border=0,fg="Black")
textfield.place(x=50,y=40)
textfield.focus()

search_icon= PhotoImage(file = "C:/Users/shree/Downloads/search-box-1-48.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command = getweather)
myimage_icon.place(x=400,y=30)

#logo
logo_image = PhotoImage(file = "C:/Users/shree/Downloads/weather-icon-png-11063.png")
logo = Label(image = logo_image)
logo.place(x = 150 , y = 100)

#bottom box 
frame_image = PhotoImage(file = "C:/Users/shree/Downloads/box.png")
frame_myimage = Label (image=frame_image)
frame_myimage.pack (padx= 5, pady=5 ,side = BOTTOM)

#time
name = Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20 ))
clock.place(x= 30 , y = 230)


#label
label1 = Label (root,text = "WIND", font = ("Helvetica",10,"bold"), fg = "white", bg = "#1ab5ef")
label1.place(x = 200, y = 400)
label1 = Label (root,text = "HUMIDITY", font = ("Helvetica",10,"bold"), fg = "white", bg = "#1ab5ef")
label1.place(x = 270, y = 400)
label1 = Label (root,text = "DISCRIPTION", font = ("Helvetica",10,"bold"), fg = "white", bg = "#1ab5ef")
label1.place(x = 430, y = 400)
label1 = Label (root,text = "PRESSURE", font = ("Helvetica",10,"bold"), fg = "white", bg = "#1ab5ef")
label1.place(x = 550, y = 400)

t = Label(font=("arial",70,"bold"),fg = "#ee666d")
t.place (x= 400 , y = 150)
c = Label(font=("arial",15,"bold"))
c.place(x=400,y = 250)



w = Label(text= "...", font =("arial",20,"bold"),bg = "#1ab5ef")
w.place(x=200,y=430)
h= Label(text= "...", font =("arial",20,"bold"),bg = "#1ab5ef")
h.place(x=280,y=430)
d = Label(text= "...", font =("arial",20,"bold"),bg = "#1ab5ef")
d.place(x=450,y=430)
p = Label(text= "...", font =("arial",20,"bold"),bg = "#1ab5ef")
p.place(x=550,y=430)


root.mainloop()

