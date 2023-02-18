import requests
import tkinter as tk

# Clé API OpenWeatherMap
API_KEY = 'VOTRE_CLÉ_API_OPENWEATHERMAP'

# Fonction pour récupérer la météo d'une ville
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=fr'
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

# Fonction pour afficher la météo dans l'interface graphique
def show_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    if weather_data['cod'] == '404':
        result_label.config(text='Ville introuvable')
    else:
        description = weather_data['weather'][0]['description'].capitalize()
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        result_label.config(text=f'{description}\nTempérature : {temperature} °C\nHumidité : {humidity}%\nVitesse du vent : {wind_speed} m/s')

# Interface graphique
root = tk.Tk()
root.title('Météo')

city_label = tk.Label(root, text='Entrez le nom de la ville :')
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

show_button = tk.Button(root, text='Afficher la météo', command=show_weather)
show_button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()
