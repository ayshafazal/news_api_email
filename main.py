import requests
from send_email import send_email

topic = "tesla"

api_key = "697bc02a008d4404a19f8de285e445ff"

url = (
    f"https://newsapi.org/v2/everything?"
    f"q={topic}&"
    "sortBy=publishedAt&"
    f"apiKey={api_key}&"
    "language=en"
)

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Create email body
body = "Subject: Today's news\n\n"

# Access the article titles and descriptions
for article in content["articles"][:20]:
    title = article.get("title")
    description = article.get("description")
    url = article.get("url")

    if title:
        body += (
            title
            + "\n"
            + (description or "No description available")
            + "\n"
            + url
            + "\n\n"
        )

# Send email
send_email(message=body.encode("utf-8"))