from urllib.parse import urljoin
import requests
import random
from bs4 import BeautifulSoup
links = [] #creates list variable named links
url = 'https://aaaa.lobadk.com/' #stores the URL to be scrapped in a variable named URL
reponse = requests.get(url) #fetches the page
soup = BeautifulSoup(reponse.text, 'lxml') #tells BS4 which parser to use
for link in soup.find_all('a'): #loops through all 'a' tags
    temp = link.get('href') #get and save the href URL to a variable named temp
    if temp.startswith('http') or temp.startswith(',') or temp.startswith('.'): #if the URL starts with comma, punctuation or is an actual link, skip
        continue
    links.append(temp) #append the URL to the links list
rng = random.randint(0, len(links)) #get a random number between 0 and the length (amount of items) in the links list
print(urljoin(url,links[rng])) #join the base URL with the relative link to create a working absolute URL, and print it