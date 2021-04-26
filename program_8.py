# This program will print the current time 
# with the help of datetime and pytz module in python.

from datetime import *
import pytz
def print_time():
    INDIA_TIME = pytz.timezone('Asia/Kolkata')
    datetime_INDIA = datetime.now(INDIA_TIME)
    print(f'India time- {datetime_INDIA.strftime("%H:%M:%S")}')
print_time()

