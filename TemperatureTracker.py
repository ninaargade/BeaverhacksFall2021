# Author: Nina Argade
# Date: 9/19/2021
# Description: This program reads the graph text file to extract the necessary data points of years and corresponding
# global land-ocean temperature indices. It will then use the matplotlib package to generate a graph of the data as a
# scatter plot with a corresponding trend line which will show that the average global temperature has been rising
# steadily since 1880, most notably within the last 20-40 years.


from matplotlib import pyplot


def main():
    """Main function reads text file containing years and corresponding temperature indices and
    displays data in a graph."""

    # read file
    file = open("graph.txt", "r")
    lines = file.readlines()
    file.close()

    # create lists of data
    year_x = []  # year
    index_y = []  # temperature index
    smoothing_y = []  # temperature index points to create trend line

    # extract data from each line of txt file
    for index, line in enumerate(lines):
        # print("line {}: {}".format(index, line.split()))
        if index >= 13:
            if int(line.split()[0]) % 5 == 0:  # 5 year increments
                year_x.append(line.split()[0])  # year
                index_y.append(float(line.split()[1]))  # temperature index
                smoothing_y.append(float(line.split()[2]))  # temperature index points to create trend line

    # plot graph with corresponding temperature indices and trend line
    pyplot.plot(year_x, index_y, 'ro', label='Annual Mean')  # scatter plot
    pyplot.plot(year_x, smoothing_y, 'go--', linewidth=2, label='Lowess Smoothing')  # trend line
    pyplot.xlabel("Year")
    pyplot.ylabel("Temperature Anomaly (°C)")
    pyplot.title("GLOBAL LAND-OCEAN TEMPERATURE INDEX")
    pyplot.legend()
    pyplot.show()


# call main function to generate graph
main()
