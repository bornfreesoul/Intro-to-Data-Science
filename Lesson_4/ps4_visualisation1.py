__author__ = 'Artemis Nika'


from pandas import *
import random
from ggplot import *
from pandasql import sqldf

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather.
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/

    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    To see all the columns and data points included in the turnstile_weather
    dataframe.

    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''

    grouped_data = turnstile_weather[["DATEn","ENTRIESn_hourly"]].groupby(["DATEn"]).sum()
    grouped_data.columns = ["ENTRIESn_daily"]
    grouped_data.index = pandas.to_datetime(grouped_data.index)
    grouped_data["DATE"] = grouped_data.index
    grouped_data.reset_index(drop=True)
    print type(grouped_data.index)
    print type(grouped_data["ENTRIESn_daily"])
    print grouped_data

    #plot = ggplot(turnstile_weather, aes(x = "ENTRIESn_hourly")) + geom_histogram() + xlab("Frequency")
    plot = ggplot(grouped_data, aes(x = "DATE", y = "ENTRIESn_daily")) + geom_point() + geom_line()
    return plot



# Test function on data
csv_file = "C:\\Users\\Pavlos-Dell\\Desktop\\Further Learning\\Udacity\\Intro to Data Science\\Lesson 3\\turnstile_data_master_with_weather.csv"
turnstile_weather = pandas.read_csv(csv_file)
rows = random.sample(turnstile_weather.index, int(len(turnstile_weather.index) * 0.15))
print plot_weather_data(turnstile_weather.ix[rows])