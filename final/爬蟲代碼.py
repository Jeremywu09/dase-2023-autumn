import requests
from bs4 import BeautifulSoup

url = 'https://shidian.baike.com/wikiid/7232179364031938621?anchor=lhq2ak6v1mwf'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    champions_table = soup.find('table', class_='champions-list')
    for row in champions_table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) > 1:  
            year = cells[0].text.strip()  
            champion = cells[1].text.strip()  
            print(f'{year}: {champion}')
else:
    print('Failed to retrieve data.')