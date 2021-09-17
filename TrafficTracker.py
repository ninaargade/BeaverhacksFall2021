# Date: September 2021

import bs4
import requests

start = "Los Angeles"
destination = "San Francisco"

# url_car = "https://google.com/search?q=time+to+get+from" + start + "to" + destination + "via+car"
url_car = "https://www.google.com/maps/dir/Long+Beach,+CA/Los+Angeles,+CA"

request_result_car = requests.get(url_car)

print(request_result_car)

soup_car = bs4.BeautifulSoup(request_result_car.text, "html.parser")

time_car = soup_car.find("div", class_='BNeawe').text

print(time_car)