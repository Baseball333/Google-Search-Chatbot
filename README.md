# Google-Search-Chatbot
This repository describes the development of a chatbot powered with omniscience and a vast amount of inputs based on the Google search engine.

First Commit:
This chatbot is based around a Python API and web interface. A chatbot is a machine learning application which can theoretically accept an infinite number of language inputs. To create such a system would require a level of effectively impossible complexity for one programmer. Luckily a superficially infinite system already exists which is fully accessible. The chatbot's input base will be the Google search engine. For this problem the basic algorithm is to perform a Google search of a user's input, scrape the text from the first result and reply to the user with the first sentence of that page's result.

Second Commit:
The chatbot must be programmed with theoretical omniscience. "Omniscience" is a characteristic of machine learning applications which pertain infinite knowledge(based on in
puts). A Python Google Search library is installed on the local directory to initiate the project. The first file is google_search.py.

Third Commit:
Once a list of URLS are established a GET request of the web page applies the Python results library. The next file is get_url.py.

Fourth Commit:
After get_url.py a file must be written to satisfy an HTTP server which is imported as a dependency. This file is called googlesearch.py.

Fifth Commit:
With google_search.py a user can accept input and complete a Google search. After the HTML is parsed the first <p> will be sorted on the page. This procedure is the rudimentary algorithm.
  
Sixth Commit:
The next phase of the project is to write an API for the chatbot's queries. The API will serve responses to the HTTP queries, whose file is server.py.

Seventh Commit:
The API is stored on port 8080 and is stored in a folder called public in the project's parent directory. The GET requests are returned from the public folder's corresponding files. GET requests will also be returned to the HTML, CSS and JavaScript stack for the web interface. This will be stored in the server.py file.
  
Eighth Commit:
After server.py is written the curl Unix command is applied locally to test the API with POST requests.
  
curl -d "How old jane doe" http://localhost:8080

The web interface stack has been written, thus the ninth commit to the README will be the last.
