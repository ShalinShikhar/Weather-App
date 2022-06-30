from cProfile import label
import json
from pydoc import describe
from tkinter import *
from tkinter import font
from urllib import request

from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import ImageTk,Image

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    city=textfield.get()
    geoLocator=Nominatim(user_agent="geoExercises")
    location=geoLocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    name.configure(text=current_time)
    clock.config(text="CURRENT WEATHER")

    #weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e603fc42376b932118915504667114b7"
    json_data=requests.get(api).json()
    condition=json_data["weather"][0]["main"]
    desccription=json_data["weather"][0]["description"]
    temp=int(json_data["main"]["temp"]-273.15)
    pressure=json_data["main"]["pressure"]
    humidity=json_data["main"]["humidity"]
    wind=json_data["wind"]["speed"]
    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    w.config(text=wind)
    d.config(text=desccription)
    h.config(text=humidity)
    p.config(text=pressure)
    
#search box
search_image=ImageTk.PhotoImage(Image.open("C:/Study/Python/Project/WeatherApp/Images/search.png"))
myLabel=Label(root,image=search_image)
myLabel.place(x=20,y=20)

textfield=Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

search_icon=ImageTk.PhotoImage(Image.open("C:/Study/Python/Project/WeatherApp/Images/search_icon.png"))
search_button=Button(root,image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
search_button.place(x=400,y=34)
#logo
logo_image=ImageTk.PhotoImage(Image.open("C:/Study/Python/Project/WeatherApp/Images/logo.png"))
logo=Label(root,image=logo_image)
logo.place(x=150,y=100)

#Bottom Box
Frame_image=ImageTk.PhotoImage(Image.open("C:/Study/Python/Project/WeatherApp/Images/box.png"))

frame_label=Label(root,image=Frame_image)
frame_label.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",10,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",10))
clock.place(x=30,y=130)


#label
label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)

c=Label(font=("arial",13,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",14,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",14,"bold"),bg="#1ab5ef")
h.place(x=250,y=430)
d=Label(text="...",font=("arial",14,"bold"),bg="#1ab5ef")
d.place(x=430,y=430)
p=Label(text="...",font=("arial",14,"bold"),bg="#1ab5ef")
p.place(x=650,y=430)


root.mainloop()
