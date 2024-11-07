#Question no 1
#Write a program that fetches and prints out a random Chuck Norris joke for the user. Use the API presented here:
# https://api.chucknorris.io/. The user should only be shown the joke text.

import requests
def get_chuck_norris_joke():
    url="https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        print(joke_data['value'])
    else:
        print("Request failed to fetch a joke. Try Again!")

get_chuck_norris_joke()


# Question No 2
#Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api. Your task is to write a
# program that asks the user for the name of a municipality and then prints out the corresponding weather condition
# description text and temperature in Celsius degrees. Take a good look at the API documentation. You must register for
# the service to receive the API key required for making API requests. Furthermore, find out how you can convert Kelvin
# degrees into Celsius.

# application programming interfaces
import requests

def get_weather(municipality, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            condition = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            print(f"Weather Condition: {condition}")
            print(f"Temperature: {temperature}°C")
        else:
            print("Failed to fetch weather data. Please try again.")

    except requests.exceptions.RequestException as e:
        print(f"Error API-request : {e}")

if __name__ == "__main__":
    api_key = "cd22e7856f3fe994027e21f9723de722"
    municipality = input("Enter the name of the municipality: ").strip()
    get_weather(municipality, api_key)


