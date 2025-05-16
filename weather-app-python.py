import tkinter as tk
import requests

API_KEY = "05c16b9271ff64d9d413383507831eff"  # Get your free key from https://openweathermap.org/api

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            result_label.config(text=f"Error: {data.get('message')}")
            return
        
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']

        result = (
            f"Weather in {city}:\n"
            f"Description: {weather_desc}\n"
            f"Temperature: {temp}°C\n"
            f"Humidity: {humidity}%"
        )
        result_label.config(text=result)

    except Exception as e:
        result_label.config(text="Error fetching data.")

# GUI Setup
root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Enter city name:").pack(pady=5)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

get_weather_btn = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
