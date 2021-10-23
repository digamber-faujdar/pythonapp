from tkinter import *
import sqlite3
import requests
import json
root=Tk()
root.title("weather app")
root.geometry("500x500")
try:
     api_request=requests.get("https://api.openweathermap.org/data/2.5/weather?zip=321202,IN&appid=ed22a3b18ec6f307f455fe381df3a3cb")
     api=json.loads(api_request.content)
except Exception as e:
     api="Error..."
kelvin=api['main']['temp']
calces=int(kelvin-273.15)
humidity=api["main"]["humidity"]
wind_ms=api["wind"]["speed"]
 
wind_km=(wind_ms*3600)/1000
 
api["name"]="konrer"
 


def temp():
     label=Label(root,text=str(calces)+"C",fg="purple")
     label.grid(row=0,column=1)
def hum():
     label=Label(root,text=str(humidity)+"%",fg="purple")
     label.grid(row=1,column=1)
def wind_k():
     label=Label(root,text=str(wind_km)+"km/h",fg="purple")
     label.grid(row=3,column=1)
def wind_m():
     label=Label(root,text=str(wind_ms)+"m/s",fg="purple")
     label.grid(row=2,column=1)
def area_name():
     label=Label(root,text=api["name"],fg="purple")
     label.grid(row=4,column=1)
def weather_rate():
     label=Label(root,text=api["weather"][0]["main"],fg="purple")
     label.grid(row=5,column=1)
def coordinate_NS():
     label=Label(root,text=api["coord"]['lon'],fg="purple")
     label.grid(row=6,column=1)
def coordinate_WE():
     label=Label(root,text=api["coord"]['lat'],fg="purple")
     label.grid(row=7,column=1)




btn_1=Button(root,text="current temprature",command=temp,bg="purple",padx=30,pady=10)
btn_1.grid(row=0,column=0)
btn_2=Button(root,text="humidity",bg="aqua",command=hum,padx=63,pady=10)
btn_2.grid(row=1,column=0)
btn_3=Button(root,text="WIND meter/sec",bg="green",command=wind_m,padx=37,pady=10)
btn_3.grid(row=2,column=0)
btn_4=Button(root,text="WIND_km/sec",bg="brown",command=wind_k,padx=45,pady=10)
btn_4.grid(row=3,column=0)
btn_5=Button(root,text="Area name",bg="gray",command=area_name,padx=56,pady=10)
btn_5.grid(row=4,column=0)
btn_6=Button(root,text="weather",bg="blue",command=weather_rate,padx=65,pady=10)
btn_6.grid(row=5,column=0)
btn_7=Button(root,text="coordinate(N-S)",bg="violet",command=coordinate_NS,padx=38,pady=10)
btn_7.grid(row=6,column=0)
btn_8=Button(root,text="coordinate(W-E)",bg="orange",command=coordinate_WE,padx=37,pady=10)
btn_8.grid(row=7,column=0)

root.mainloop()
