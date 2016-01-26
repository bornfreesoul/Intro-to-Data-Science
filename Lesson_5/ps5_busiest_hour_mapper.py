__author__ = 'Artemis Nika'


import sys
import string
import logging

logging.basicConfig(filename = "mapper_logfile.txt", format = '%(message)s',
                    level = logging.INFO, filemode = 'w')

def mapper():
    """
    In this exercise, for each turnstile unit, you will determine the date and time
    (in the span of this data set) at which the most people entered through the unit.

    The input to the mapper will be the final Subway-MTA dataset, the same as
    in the previous exercise. You can check out the csv and its structure below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    For each line, the mapper should return the UNIT, ENTRIESn_hourly, DATEn, and
    TIMEn columns, separated by tabs. For example:
    'R001\t100000.0\t2011-05-01\t01:00:00'

    Since you are printing the output of your program, printing a debug
    statement will interfere with the operation of the grader. Instead,
    use the logging module, which we've configured to log to a file printed
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    """
    header = sys.stdin.readline().strip().split(",")
    #logging.info(" ".join(header))
    unit_ind = header.index("UNIT")
    entries_ind = header.index("ENTRIESn_hourly")
    date_ind = header.index("DATEn")
    time_ind = header.index("TIMEn")

    for line in sys.stdin:
        tokens = line.strip().split(",")
        if len(tokens) != 21:
            next
        print '{0}\t{1}\t{2}\t{3}'.format(tokens[unit_ind], tokens[entries_ind], tokens[date_ind], tokens[time_ind])
        #logging.info('{0}\t{1}\t{2}\t{3}'.format(tokens[unit_ind], tokens[entries_ind], tokens[date_ind], tokens[time_ind]))
mapper()

# from cmd
#python .\ps5_busiest_hour_mapper.py < turnstile_data_master_with_weather.csv|sort|python .\ps5_busiest_hour_reducer.py
