import requests
from bs4 import BeautifulSoup
import re
import time

# Get Bitcoin Price
URL= 'https://www.coindesk.com/price/bitcoin'
# Set an alarm for your price (For example 56 is $56,000)
YOUR_PRICE=56
# You Slack Hook
SLACK_URL='YOUR_SLACK_HOOK'
my_header={'Content-type':'application/json'}
my_payload='{"text":"Bitcoin Price Alaram"}'

while('true'):
    # Fetch Bitcoin price
    response = requests.get(URL)
    my_soup = BeautifulSoup(response.content, 'html.parser')
    price=my_soup.find_all('div','price-large')
    # Filter price
    price=(re.sub("[a-z\s=<>\"$/\[\]-]", "",str(price))[:6])
    print("$ "+price)
    if (int(price[:2]) == YOUR_PRICE):
        requests.post(SLACK_URL,data=my_payload,headers=my_header)
        break

    # Send requests each 30 seconds for fetching price
    time.sleep(30)