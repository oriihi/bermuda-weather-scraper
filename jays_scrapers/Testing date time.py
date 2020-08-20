from datetime import datetime,timedelta #for setting times
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%y/%m/%d %H:%M")
print("date and time =", dt_string)	
