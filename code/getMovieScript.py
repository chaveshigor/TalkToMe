from bs4 import BeautifulSoup
import requests

movie = "Joker"
link = 'https://www.imsdb.com/scripts/'+ movie +'.html'

myResponse = requests.get(link).text

soup = BeautifulSoup(myResponse, 'html.parser')
print(soup.body.table)