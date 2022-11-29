SECONDS_PER_MINUTE  = 60
SECONDS_PER_HOUR    = 3600
SECONDS_PER_DAY     = 86400
 
seconds = int(input("Enter number of seconds:"))
 
days = seconds / SECONDS_PER_DAY
seconds = seconds % SECONDS_PER_DAY
 
hours = seconds / SECONDS_PER_HOUR
seconds = seconds % SECONDS_PER_HOUR
 
minutes = seconds / SECONDS_PER_MINUTE
seconds = seconds % SECONDS_PER_MINUTE
print("The duration is: ","%d:%02d:%02d:%02d"%(days,hours,minutes,seconds))
