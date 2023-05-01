import requests

# declare the creds
api_key = "fb0941afa24d4e18a8f3b6b0d9163c19"
url = "https://newsapi.org/v2/top-headlines?" \
      "sources=techcrunch&" \
      "apiKey=fb0941afa24d4e18a8f3b6b0d9163c19"

# Access the url
request = requests.get(url)

# Get the content
content = request.json()

# Print the articles
for article in content["articles"]:
    print(article['title'])
    print(article['description'])

# Download an image
image_url = "https://images.news18.com/ibnlive/uploads/2021/06/1623315104_new-kia-sportage-5.png?" \
            "impolicy=website&width=510&height=356"
response = requests.get(image_url)
with open("kia-sportage.png", "wb") as file:
      file.write(response.content)

