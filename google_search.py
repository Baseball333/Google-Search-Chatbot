from googlesearch import search

query = "How old is Jane Doe"

# Query the results into a list of URLS
search_result_list = list(search(query, tld="co.in", num=10, stop=3, pause=1))

