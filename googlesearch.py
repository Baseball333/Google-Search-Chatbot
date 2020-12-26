import requests
import string
from lxml import search
from bs4 import BeautifulSoup

# To search print the query method
def chatbot_query(query, index=0):
    fallback = "Sorry, I cannot think of a reply for that."
    result = ""
    
    try:
