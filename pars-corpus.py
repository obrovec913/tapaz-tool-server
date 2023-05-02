import requests

url = 'https://ruscorpora.ru/search-ngrams.php'
data = {
    'text': 'тайгер',  # Replace with the search term
    'mode': 'main',
    'sort': 'gr_tagging',
    'lang': 'ru',
    'req': 'example',  # Replace with the search term
    'out': 'normal',
    'maxpassages': '10',
    'findsimilar': 'on',
    'method': 'baw',
    'pregenerated': '0'
}

response = requests.post(url, data=data)
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'lxml')

# Find the search results container
results = soup.find('div', {'class': 'search_results'})

# Extract the search results
for result in results.find_all('div', {'class': 'result'}):
    # Extract relevant data from the result, such as the text and context
    print(result.find('span', {'class': 'b-wrd'}).text)


