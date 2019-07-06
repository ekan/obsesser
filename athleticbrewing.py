import requests
from bs4 import BeautifulSoup

# this doesn't work because of javascript voodoo, the locations list loads with AJAX after the page loads
# there's a way to do this, for now just inspecting the element and copying/pasting to a file
#page = requests.get('https://www.athleticbrewing.com/where-to-find-us')
soup = BeautifulSoup(open('in/athleticbrewing_190705.html'), 'html.parser')

locList = soup.find_all(class_='storepoint-location')

for loc in locList:
    name = loc.find(class_='storepoint-name').text
    addr = loc.find(class_='storepoint-address').text
    print('\"'+name+'\",\"'+addr+'\"')

