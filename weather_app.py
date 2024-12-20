import requests
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Constants
API_KEY = "6a0f6202e4d6cf4dd65019ab26f780ec"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data for a given city."""
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"  # For temperature in Celsius
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"{Fore.RED}Error: {data.get('message', 'Unable to fetch weather data.')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error: {e}")
        return None

def display_weather(data):
    """Display weather data in a colorful and readable format."""
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    weather_desc = data['weather'][0]['description'].capitalize()
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"\n{Fore.CYAN}{Style.BRIGHT}Weather in {city}, {country}")
    print(f"{'-'*30}")
    print(f"{Fore.YELLOW}Temperature: {Fore.GREEN}{temp}°C")
    print(f"{Fore.YELLOW}Condition: {Fore.GREEN}{weather_desc}")
    print(f"{Fore.YELLOW}Humidity: {Fore.GREEN}{humidity}%")
    print(f"{Fore.YELLOW}Wind Speed: {Fore.GREEN}{wind_speed} m/s")
    print(f"{'-'*30}")

def main():
    """Main function to run the weather application."""
    print(f"{Fore.BLUE}{Style.BRIGHT}Welcome to the Weather Forecast Application!")
    while True:
        city = input(f"\n{Fore.CYAN}Enter the city name (or type 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print(f"{Fore.MAGENTA}Goodbye! Stay safe and enjoy your day!")
            break

        print(f"{Fore.GREEN}Fetching weather data for {city}...")
        weather_data = get_weather(city)

        if weather_data:
            display_weather(weather_data)

if __name__ == "__main__":
    main()
