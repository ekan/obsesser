import requests
from bs4 import BeautifulSoup

page = requests.get('https://motherdirt.com/apps/store-locator')
soup = BeautifulSoup(page.text, 'html.parser')

locList = soup.find("div",{"id":"addresses_list"})
locListItems = locList.find_all('li')

for loc in locListItems:
    name = loc.find(class_='name').text.lstrip()
    addr = loc.find(class_='address').text.lstrip()
    city = loc.find(class_='city').text.lstrip()
    if(loc.find(class_='postal_zip')):
        zip = loc.find(class_='postal_zip').text.lstrip()
    else:
        zip = ""
    print('\"'+name+'\",\"'+addr+'\",\"'+city+'\",\"'+zip+'\"')

