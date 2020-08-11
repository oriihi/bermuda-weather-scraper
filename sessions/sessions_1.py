from datetime import datetime, date, time, timedelta #for setting times

my_sesh_date = input('Enter a date (i.e. 2020,7,1)')
year, month, day = map(int, my_sesh_date.split(','))
date = datetime(year, month, day)

my_sesh_start_time = input('Enter sesh start time (i.e. 09:30)')
hours, minutes = map(int, my_sesh_start_time.split(':'))
start_time = time(hours, minutes)

my_sesh_time_length = input('Enter a time (i.e. 1.5)hrs')
hours, minutes = map(int, my_sesh_time_length.split('.'))
time_length = time(hours, minutes)