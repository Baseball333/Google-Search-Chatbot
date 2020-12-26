import requests
from  import html
from googlesearch import search
from bs4 import BeautifulSoup

query = "How old is Jane Doe"

# Query search results as a Python list of URLs
search_result_list = list(search(query, tld="co.in", num=10, stop=3, pause=1))

page = requests.get(search_result_list[index])

tree = html.fromstring(page.content)

soup = BeautifulSoup(page.content, features="lxml")
