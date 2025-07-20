
#             MINI PROJECT

''' 1.	create a python program that asks the user how far they want to travel. if they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell them to driver Super-Car.
Sample Output:
How far would you like to travel in miles? 2500
I suggest Super-Car to your destination'''

dis=float(input("How far would you like to travel in miles:  "))
if dis<3:
    print("I suggest Biycal to your destination")
elif dis>3 and dis<300:
    print("I suggest ride Motor-cycle  to your destination")
else:
    print("I suggest Super-Car to your destination")

'''2.	Let's assume you are planning to use your python skills to build an App for Mobile.
You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
Write a python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How much days can I operate one server with $918?'''



one_hour_cost = 0.51
daily_hours = 24
budget = 918
daily_cost = one_hour_cost * daily_hours
weekly_cost = daily_cost * 7
monthly_cost = daily_cost * 30
affordable_days = budget / daily_cost
print("=== Server Cost Estimation ===")
print("Daily Cost   : $", round(daily_cost, 2))
print("Weekly Cost  : $", round(weekly_cost, 2))
print("Monthly Cost : $", round(monthly_cost, 2))
print()
print("With $", budget, ", you can run the server for about", round(affordable_days, 2), "days.")



