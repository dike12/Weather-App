# Import required libraries
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# Import the API key from the config file
from config import API_KEY


# Initialize the main window
root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")  # Set the size and position of the window
root.resizable(False, False)       # Disables resizing of the window

# Function to fetch and display weather information
def getWeather():
    try:
        city = textfield.get()  # Get the city name entered by the user

        # Use Nominatim geolocator to get location details
        geolocator = Nominatim(user_agent="myWeather")
        location = geolocator.geocode(city)

        # Find the timezone of the location
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)

        # Get the current time in the location's timezone
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # Prepare the API request for weather data
        api = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location.latitude},{location.longitude}"
        json_data = requests.get(api).json()

        # Extract weather data from the API response
        condition = json_data["current"]["condition"]["text"]
        temp = json_data["current"]["temp_c"]
        pressure = json_data["current"]["pressure_mb"]
        humidity = json_data["current"]["humidity"]
        wind = json_data["current"]["wind_kph"]

        # Update the UI with the weather data
        t.config(text=f"{temp}°")
        c.config(text=f"{condition} | FEELS LIKE {temp}°")
        w.config(text=f"{wind} kph")
        h.config(text=f"{humidity}%")
        d.config(text=condition)
        p.config(text=f"{pressure} mb")
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!!")  # Show error on invalid input

# Set up the search box
search_image = PhotoImage(file="search.png")
myimage = Label(image=search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()  # Focus on the textfield

search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# Set up the logo
logo_image = PhotoImage(file="logo.png")
logo = Label(image=logo_image)
logo.place(x=150, y=100)

# Set up the bottom box
frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Set up labels for time and weather data
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

label1 = Label(root, text="Wind", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)
label2 = Label(root, text="Humidity", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)
label3 = Label(root, text="Description", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)
label4 = Label(root, text="Pressure", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

# Set up labels for displaying weather data
t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)
w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

# Start the Tkinter main loop
root.mainloop()
