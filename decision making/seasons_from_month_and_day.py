month = input("Month=")
day = int(input("Day:"))

if month in ('january','feburary','march'):
	season = "winter"
elif month in ('april', 'may', 'june'):
	season = "spring"
elif month in ('july', 'august', 'september'):
	season = "summer"
else:
	season = 'autumn'

if (month == 'march') and (day > 19):
	season = "spring"
elif (month == 'june') and (day > 20):
	season = "summer"
elif (month == 'september') and (day > 21):
	season = "autumn"
elif (month == 'december') and (day > 20):
	season = "winter"

print("Season is",season)