import re
from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/live/2022/09/06/us/weather-forecast-news-summer"

result = requests.get(url)
print(result.text)
