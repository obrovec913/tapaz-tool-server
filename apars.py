from gettext import find
import re
from bs4 import  BeautifulSoup as bs
import requests

he =  {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

def savePars(fi: str, words:str, ):
    o = open(f'dictionary\\1{words}.txt', 'a+', encoding='utf-8')
    so = bs(fi, "lxml")
    results = so.find( class_='kwic-list')
    print()
    # Extract the search results
    for result in results.find_all(class_='hit word'):
    # Extract relevant data from the result, such as the text and context
      o.write(f'{words} : {result.text}\n')    



if __name__ == "__main__":
    pass