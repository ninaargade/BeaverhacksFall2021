# Date: September 2021

import bs4
import requests

from matplotlib import pyplot


# start = "Imphal"
# destination = "San Francisco"

# url_car = "https://google.com/search?q=time+to+get+from" + start + "to" + destination + "via+car"
# url_car = "https://google.com/search?q=weather+in+" + start

# url_car = "https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt"
#
# request_result_car = requests.get(url_car)
#
# print(request_result_car)
#
# soup_car = bs4.BeautifulSoup(request_result_car, "html.parser")
#
# # time_car = soup_car.find("div", class_='BNeawe').text
#
# print(soup_car)

def main():
    file = open("graph.txt", "r")
    lines = file.readlines()
    file.close()

    year_x = []
    index_y = []
    smoothing_y = []

    for index, line in enumerate(lines):
        print("line {}: {}".format(index, line.split()))
        if index >= 5:
            if int(line.split()[0]) % 10 == 0:
                year_x.append(line.split()[0])
                index_y.append(float(line.split()[1]))
                smoothing_y.append(float(line.split()[2]))

    print(year_x)
    print(index_y)

    # plot graph with corresponding sort function times for both series of data points
    pyplot.plot(year_x, index_y, 'ro--', label='Bubble Sort')
    pyplot.plot(year_x, smoothing_y, 'go--', linewidth=2, label='Insertion Sort')
    pyplot.xlabel("Year")
    pyplot.ylabel("Temperature Anomaly (C)")
    pyplot.legend()
    pyplot.show()


main()