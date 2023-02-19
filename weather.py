import requests
import tkinter as tk

# OpenWeatherMap API KEY
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

# Get the weather of the city
def get_weather(city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=fr'
        response = requests.get(url)
        response.raise_for_status()  # Check for errors
        return response.json()
    except requests.exceptions.HTTPError:
        return {'cod': '404'}

# Display weather with Tkinter
def show_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    if weather_data['cod'] == '404':
        result_label.configure(text='Untraceable City', font=('Arial', 12, 'bold'))
    else:
        description = weather_data['weather'][0]['description'].capitalize()
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        result_label.configure(text=f'{description}\nTemperature: {temperature} °C\nHumidity: {humidity}%\nWind speed: {wind_speed} m/s', font=('Arial', 12))

# Graphic interface
root = tk.Tk()
root.title('Weather - natrix')

city_label = tk.Label(root, text='Enter the name of the city:', font=('Arial', 12))
city_label.pack()

city_entry = tk.Entry(root, font=('Arial', 12))
city_entry.pack()

show_button = tk.Button(root, text='Display the weather', command=show_weather, font=('Arial', 12, 'bold'))
show_button.pack()

result_label = tk.Label(root, text='', font=('Arial', 12))
result_label.pack()

root.mainloop()
