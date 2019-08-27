import urllib.request
from bs4 import BeautifulSoup

file = open('test.md', 'w+')

url = "https://en.wikipedia.org/wiki/Call_of_Duty:_Infinite_Warfare"
source = urllib.request.urlopen(url)
soup = BeautifulSoup(source, 'html.parser')

# Getting the first paragrapg
# first_paragraph = soup.p.getText()
# print(first_paragraph)

# Getting all the links in the webpage
# links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))

# Getting all the image links from the webpage
# images_link = soup.find_all('img')
# for image in images_link:
#     file.write("![alt](https://" + image.get('src') + ")")

# Getting table contents and printing them out
table = soup.find('table', {'class' : 'hproduct'})
table_rows = table.find_all('tr')

for row in table_rows:
    if row.find('th') == None : continue

    file.write('- ' + row.find('th').getText() + '\n')

    for item in row.find_all('td'):
        file.write('  - ' + item.getText() + '\n')

file.close()        