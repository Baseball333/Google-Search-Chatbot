import requests
import string
from lxml import search
from bs4 import BeautifulSoup

# To search print the query method
def chatbot_query(query, index=0):
    fallback = "Sorry, I cannot think of a reply for that."
    result = ""
    
    try:
      search_result_list = list(search(query, tld="co.in", num=10, stop=3, pause=1))

      page = requests.get(search_result_list[index])
        
      tree =  html.fromString(page.content)
    
      soup = BeautifulSoup(page.content, features="lxml")
    
