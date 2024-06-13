#=======================#
# IMPORT PACKAGE
#=======================#
# from geopy.geocoders import nominatim
# from timezonefinder import TimezoneFinder
from tkinter import*
import tkinter as tk
from tkinter import ttk,messagebox
from datetime import datetime
import requests
import pytz

# import functin_temp
#=======================#
# Main window
#=======================#

root=Tk()
root.title('Weather App')
root.geometry('900x500+300+200')
root.resizable(False,False)





#=======================#
#  FUNCTION
#=======================#

def getweather():
    city = textfield.get()
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=496edb21c74fe7b933eec419e5ce8985"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        if data["cod"] == 200:  # Check if API response is successful
            # Extract weather information from the API response
            temperature_kelvin = data["main"]["temp"]
            temperature_celsius = temperature_kelvin - 273.15
            weather_description = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]

            # Update the labels with weather information
            t.config(text=f"{temperature_celsius:.1f}°C")
            w.config(text=f"{wind_speed} m/s")
            h.config(text=f"{humidity}%")
            d.config(text=weather_description)
            p.config(text=f"{pressure} hPa")
        else:
            messagebox.showerror("Error", "City not found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


#=======================#
#  WEATHER
#=======================#







#=======================#
#  Search Box
#=======================#
search_image=PhotoImage(file="./image/search.png")
myimage=Label(image=search_image)
myimage.place(x=14,y=20)
textfield=tk.Entry(root,justify="center",width=20,font=("poppins",25,"bold"),bg="#404040",fg="white",borderwidth=0,takefocus = 0)
textfield.place(x=50,y=40)
textfield.focus()

search_icon=PhotoImage(file="./image/search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myimage_icon.place(x=400,y=34)

#=======================#
#  LOGO
#=======================#

logo_image=PhotoImage(file="./image/logo.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)

#=======================#
#  BOTTOM BOX
#=======================#

frame_image=PhotoImage(file="./image/box.png")
frame_myimage=Label(image=frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)
#=======================#
#  BOTTOM BOX
#=======================#

name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100 )
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)


#=======================#
#  LABEL
#=======================#

label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDTY",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg='#ee666d')
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)

root.mainloop()
