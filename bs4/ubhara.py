import json
from contextlib import redirect_stdout
from bs4 import BeautifulSoup
import requests


html_doc = requests.get('https://www.ubhara.ac.id/v3/p/kemahasiswaan')
soup = BeautifulSoup(html_doc.text, 'html.parser')

# print(soup.prettify())

# with open('out.txt', 'w') as f:
#     with redirect_stdout(f):
#         print(soup.prettify())

judul = []
isi = []

a = soup.select('div.panel > div.panel-heading > h3 ')

# print(a)
for ab in a:
    judul.append(ab.get_text())

b = soup.select('div.panel-body > ul')
# print(b)

# z = b[].select('ul > li')
# # print(z)

for bc in b:
    temp = []
    for bd in bc.select('ul > li'):
        temp.append(bd.get_text())
    isi.append(temp)

y = []
for x in range(5):
    y.append({
        'Judul': judul[x],
        'Isi': isi[x]
    })

# print(y)

# Serializing json
json_object = json.dumps(y, indent=4)

# Writing to sample.json
with open("output.json", "a") as outfile:
    outfile.write(json_object)
