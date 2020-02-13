# Weekly taks 5, weekday checker
# import datetime module
import datetime
# create an object with todays date
td = datetime.datetime.now()
# create object with todays day of the weeks int index
wd = td.weekday()

# create a list with the days of the week in order
days = ["Monday", "Tuesday", "Wednesday", "Thursday",
"Friday", "Saturday", "Sunday"]
# if todays day is 0,1,2,3 or 4, its a weekday
if wd < 5:
	print("Yes, unfortunately today is a weekday, It's", days[wd])
# if the day is 5 or more then its saturday or sunday
elif wd > 4:
	print("It is the weekend, YAY! It's", days[wd])
