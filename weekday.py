# Cian Hogan
# Weekly task 5, weekday checker
# import datetime module
import datetime
# create an object with an index for todays day
day = datetime.datetime.now().weekday()

# create a list with the days of the week in order
days = ["Monday", "Tuesday", "Wednesday", "Thursday",
"Friday", "Saturday", "Sunday"]
# if todays day is 0,1,2,3 or 4, its a weekday
if day < 5:
	print("Yes, unfortunately today is a weekday, It's", days[day])
# if the day is 5 or more then its saturday or sunday
elif day > 4:
	print("It is the weekend, YAY! It's", days[day])
