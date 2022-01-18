#!/usr/bin/env python3

# Coding test: Parse a (syslog) file to get various fields
# from the logs and message counts. Associate counts
# with the processes that logged them...

# You are given some logs with timestamp, process
# ids, log statement. You need to parse the the log file
# and print out in two columns the time stamp and the
# number of times the same process (or thereabout)
# shows up in the same time stamp (in other words
# column A has the time stamp, column B has the count).
# I think this needed to be outputted in CSV or
# something, but interviewer mentioned it didn't really
# matter.

### Example contents of Apple Mac syslog ###
# Nov 30 00:23:15 Davids-Mac-mini syslogd[332]: ASL Sender Statistics
# Nov 30 00:27:40 Davids-Mac-mini login[3783]: USER_PROCESS: 3783 ttys004
# Nov 30 00:30:05 Davids-Mac-mini syslogd[332]: Configuration Notice:
############################################

import glob
import os
import re
import time

from datetime import datetime, timedelta, timezone

# find any files in current dir that match the filename pattern below,
files = glob.glob('*.log')

now = datetime.now()  # current date and time, defaults to current locale timezone
now_utc = datetime.now(timezone.utc)  # current date and time, in UTC

# datetime.strptime() can be used to create a datetime object from a given string 
# (such as a string that ordinarily represents a date, a time, a datetime, a timestamp, ...).

# datetime.strftime() can be used to create a string from a datetime object.

# datetime.utcfromtimestamp(posix_timestamp) can return a datetime object from a POSIX timestamp

# datetime.utcoffset() can be used to return the UTC offset

# Some relevant formatting codes:
# %Y%m%d%H%M%S

# print out the attributes (methods) of the datetime class:
print(dir(datetime))

# You can subtract a datetime object against another one, and the result is a timedelta object
now = datetime.now(timezone.utc)
time.sleep(1.5)
now2 = datetime.now(timezone.utc)
new_timedelta_obj = now2 - now

# a timedelta object has an attribute for calculating total seconds:
print(new_timedelta_obj.total_seconds())
t = timedelta(days=3, hours=1, minutes=4, seconds=1)
print(t.total_seconds())

def parse_mac_syslog():
    log_lines = []
    with open('/var/log/system.log', 'r') as file_r:
        for line in file_r:
            # filter out log lines that start with a tab char
            if not '\t' in rf'{line}':
                log_lines.append(line)

    # for line in log_lines:
    #     print(line, end="\n")
    # print(log_lines[0:30])

    parsed_data = []
    data = {}
    prev_tstamp = ""

    for line in log_lines:
        proc_name = line.split()[3]

        # make tstamp string
        tstamp = " ".join(line.split()[0:3])

        if prev_tstamp != "":

            print(f"Comparing tstamps: {prev_tstamp} - {tstamp}")
            if tstamp == prev_tstamp:
                data[tstamp]["count"] = data[tstamp]["count"] + 1
                if proc_name in data[tstamp]:
                    data[tstamp][proc_name] = data[tstamp][proc_name] + 1
            else:
                prev_tstamp = tstamp
                parsed_data.append(data)
                data = {}
                data[tstamp] = {"count": 1, proc_name: 1}
        else:
            prev_tstamp = tstamp
            data[tstamp] = {"count": 1, proc_name: 1}

    for i in parsed_data:
        print(i)

# tail a continuously updating file
def file_read_and_follow(name):
    current = open(name, "r")
    curino = os.fstat(current.fileno()).st_ino
    while True:
        while True:
            line = current.readline()
            if not line:
                break
            yield line

        try:
            if os.stat(name).st_ino != curino:
                new = open(name, "r")
                current.close()
                current = new
                curino = os.fstat(current.fileno()).st_ino
                continue
        except IOError:
            pass
        time.sleep(1)

if __name__ == "__main__":
    parse_mac_syslog()

    fname = "/Users/davidgibney/test.log"
    for l in file_read_and_follow(fname):
        print( "LINE: {}".format(l))
