from bs4 import BeautifulSoup
import requests

url = 'https://fitnesspoint.no/vare-senter/fitnesspoint-malvik/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

# <div style="display:block; padding: 10px; background: #93117d; color: #fff; font-size: 20px; font-weight: bold; margin-bottom: 30px;" class="fp-location-visitors" data-location="20">Antall besøkende: 1 / 17</div> 
content = soup.find('div', class_='fp-location-visitors').contents
fp_location_visitors = content[0].lstrip().rstrip()
print(fp_location_visitors)