import requests
from send_email import send_email
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=697bc02a008d4404a19f8de285e445ff')

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)