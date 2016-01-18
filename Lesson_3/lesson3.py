import scipy.stats


#scipy.stats.ttest_ind(a, b, equal_var = False)

import numpy
import scipy.stats
import pandas

def compare_averages(filename):
    """
    Performs a t-test on two sets of baseball data (left-handed and right-handed hitters).

    You will be given a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg'). You can look at the csv
    file by downloading the baseball_stats file from Downloadables below. 
    
    Write a function that will read that the csv file into a pandas data frame,
    and run Welch's t-test on the two cohorts defined by handedness.
    
    One cohort should be a data frame of right-handed batters. And the other
    cohort should be a data frame of left-handed batters.
    
    We have included the scipy.stats library to help you write
    or implement Welch's t-test:
    http://docs.scipy.org/doc/scipy/reference/stats.html
    
    With a significance level of 95%, if there is no difference
    between the two cohorts, return a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.  
    
    If there is a difference, return a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.
    
    For example, the tuple that you return may look like:
    (True, (9.93570222, 0.000023))
    """

    df = pandas.read_csv(filename)
    rh_avg = df[df["handedness"] == "R"]["avg"]
    #print rh_avg
    lh_avg = df[df["handedness"] == "L"]["avg"]
    #print lh_avg

    t_test_result = scipy.stats.ttest_ind(rh_avg, lh_avg, equal_var = False)
    #print t_test_result[1] < 0.05
    return [not t_test_result[1] < 0.05, t_test_result]

print compare_averages("baseball_stats.csv")
