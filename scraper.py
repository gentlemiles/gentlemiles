import requests
from bs4 import BeautifulSoup

# The URL of the website we want to scrape
url = 'http://quotes.toscrape.com/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the quote containers
    quotes = soup.find_all('div', class_='quote')

    # Loop through each quote and extract the text and author
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f'"{text}" - {author}')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
