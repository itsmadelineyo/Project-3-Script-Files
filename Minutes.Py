>>> def calculate_minutes(years):
...     # 1 year = 365 days, 1 day = 24 hours, 1 hour = 60 minutes
...             minutes = years * 365 * 24 * 60
...             return minutes
...
>>> years = int(input("Enter number of years: "))
Enter number of years: 5
>>> minutes = calculate_minutes(years)
>>> print("Number of minutes in", years, "years is:", minutes)
Number of minutes in 5 years is: 2628000
>>>
