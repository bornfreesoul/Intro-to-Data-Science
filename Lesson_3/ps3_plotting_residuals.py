__author__ = 'Artemis Nika'

import numpy as np
import scipy
import pandas
import matplotlib.pyplot as plt
import random
import ps3_regression_gradient_descent as p3


def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''

    plt.figure()
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist(bins = 150, alpha = 0.8)
    x1,x2,y1,y2 = plt.axis()
    plt.axis([x1, x2, y1, y2])
    #plt.legend()
    plt.title("Histogram of Residuals")
    plt.xlabel("Residuals")
    plt.ylabel("Frequency")
    return plt


dataframe = pandas.read_csv(
    "C:\\Users\\Pavlos-Dell\\Desktop\\Further Learning\\Udacity\\Intro to Data Science\Lesson 3\\turnstile_data_master_with_weather.csv")

# choose subset of dataframe

rows = random.sample(dataframe.index, int(0.15 * len(dataframe.index)))

pred, plot = p3.predictions(dataframe.ix[rows])
print "pred", pred
resPlot = plot_residuals(dataframe.ix[rows], pred)

print resPlot.show()
