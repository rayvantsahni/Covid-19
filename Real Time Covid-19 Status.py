import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"

page = requests.get(url)
page = page.text
soup = BeautifulSoup(page, 'html.parser')

print("\033[1m" + "COVID-19 Status of the World" + "\033[0m\n")

x1 = soup.findAll('h1')
x2 = soup.findAll("div", {"class": "maincounter-number"})
    
for i, j in zip(x1, x2):
    print(i.text, j.text)
    
x3 = soup.findAll("span", {"class": "panel-title"})
x4 = soup.findAll("div", {"class": "number-table-main"})

for i, j in zip(x3, x4):
    _i = i.text.strip()
    _j = j.text.strip()
    print(_i, _j, sep = ":\n", end = "\n\n")
    
x5 = soup.find("div", {"style": "font-size:13px; color:#999; margin-top:5px; text-align:center"})
print(x5.text)


y_or_n = input("Do you want to check the status of any particular country? (y/n)")

if y_or_n == 'Y' or y_or_n == 'y':
    country = input("Enter the country name:\n")

    url = "https://www.worldometers.info/coronavirus/country/" + country.lower().replace(" ", "-") + "/"

    page = requests.get(url)
    page = page.text
    soup = BeautifulSoup(page, 'html.parser')

    print("\nThe current status of ", country, " is:", sep = "")

    y = soup.findAll("div", {"id": "maincounter-wrap"})
    for i in y:
        print(i.text, end = "")
        
if y_or_n == 'N' or y_or_n == 'n':
    print("OK then. Good bye. Stay safe..")
