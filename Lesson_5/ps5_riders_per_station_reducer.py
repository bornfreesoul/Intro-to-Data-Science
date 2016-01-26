__author__ = 'Artemis Nika'


import sys
import logging


logging.basicConfig(filename = "reducer_logfile.txt", format = '%(message)s',
                    level = logging.INFO, filemode = 'w')

def reducer():
    '''
    Given the output of the mapper for this exercise, the reducer should PRINT
    (not return) one line per UNIT along with the total number of ENTRIESn_hourly
    over the course of May (which is the duration of our data), separated by a tab.
    An example output row from the reducer might look like this: 'R001\t500625.0'

    You can assume that the input to the reducer is sorted such that all rows
    corresponding to a particular UNIT are grouped together.

    Since you are printing the output of your program, printing a debug
    statement will interfere with the operation of the grader. Instead,
    use the logging module, which we've configured to log to a file printed
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''
    old_key = None
    aggr = 0

    for line in sys.stdin:
        new_key, value = line.strip().split("\t")
        value = float(value)
        if old_key == None:
            old_key = new_key
        elif old_key != new_key:
            print "{0}\t{1}".format(old_key, aggr)
            old_key = new_key
            aggr = value
        else:
            aggr += value
    print "{0}\t{1}".format(old_key, aggr)

reducer()


# to run map-reduce job in cmd
# python ps5_riders_per_station_mapper.py < turnstile_data_master_with_weather.csv | sort | python ps5_riders_per_station_reducer.py
