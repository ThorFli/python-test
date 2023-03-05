import requests
from bs4 import BeautifulSoup

city = 'Hamburg'
url = f'https://sonnenaufgang.online/sun/{city}'
#url = f'https://zwiftpower.com/profile.php?z=4516687'
## url = f'https://sonnenaufgang.online/sun/larvik'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
#print(response.text)


sunrise_data = soup.find('div', {'data-name': 'sunrise'})
sunrise_data = sunrise_data.text
sunrise_data = sunrise_data[:-3]
print(f'Die Sonne geht in {city} heute um {sunrise_data} auf.')

