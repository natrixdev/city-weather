import requests
import tkinter as tk

# OpenWeatherMap API KEY
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY'

# Get the weather of the city
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=fr'
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

# Display weather with Tkinter
def show_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    if weather_data['cod'] == '404':
        result_label.config(text='Untraceable City')
    else:
        description = weather_data['weather'][0]['description'].capitalize()
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        result_label.config(text=f'{description}\nTemperature : {temperature} °C\nHumidity : {humidity}%\nWind speed : {wind_speed} m/s')

# Graphic interface
root = tk.Tk()
root.title('Weather - natrix')

city_label = tk.Label(root, text='Enter the name of the city :')
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

show_button = tk.Button(root, text='Display the weather ', command=show_weather)
show_button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()
