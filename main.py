import requests
from bs4 import BeautifulSoup


def get_weather_report(city: str):
    """Prints weather report for a particular city."""
    weather_url = f"https://www.google.com/search?q=weather+{city}"
    html = requests.get(weather_url).content

    # Create soup from HTML data
    soup = BeautifulSoup(html, 'html.parser')
    temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    current_data = soup.find(
        'div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    time, sky = current_data.split('\n')[0], current_data.split('\n')[1]

    # getting all div tags
    all_divs = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    weather_desc = all_divs[5].text

    index = weather_desc.find('Wind')
    desc = weather_desc[:index]
    other_data = weather_desc[index:]

    print()
    print("Current Time: "+time)
    print("Current Temperature: "+temperature)
    print("Sky: "+sky)
    print("Description: "+desc)
    print("Other Data: "+other_data)


if __name__ == '__main__':
    city = input("Enter city name: ")
    get_weather_report(city)
