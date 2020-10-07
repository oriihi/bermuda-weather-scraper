from datetime import datetime,timedelta #for setting times
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
#print("now =", now)

# dd/mm/YY H:M:S
now_time_gsheet = now.strftime("%Y/%m/%d %H:%M")
print("date and time =", now_time_gsheet)	
