print("TODO: make a web request for some stock")

import os
from dotenv import load_dotenv
import requests
import json 
load_dotenv() # go get env vars from the .env file
# read env variables
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
# make a request
symbol = "MSFT" # ask for a user input
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(request_url)
# print(type(response)) #> <class 'requests.models.Response'> 
# print(response.status_code) #> 200
# print(response.text) # string, so need to use json to process into dictionary 

# parse response.text from string to dictionary
parsed_response = json.loads(response.text)
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")