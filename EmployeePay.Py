>>> def calculate_weekly_pay(hourly_wage, regular_hours, overtime_hours):
...     regular_pay = hourly_wage * regular_hours
...     overtime_pay = overtime_hours * (1.5 * hourly_wage)
...     total_pay = regular_pay + overtime_pay
...     return total_pay
...
>>> hourly_wage = float(input("Enter the hourly wage: "))
Enter the hourly wage: 17.50
>>> regular_hours = float(input("Enter the total regular hours worked: "))
Enter the total regular hours worked: 80.75
>>> overtime_hours = float(input("Enter the total overtime hours worked: "))
Enter the total overtime hours worked: 8
>>> total_weekly_pay = calculate_weekly_pay(hourly_wage, regular_hours, overtime_hours)
>>> print(f"Total weekly pay: ${total_weekly_pay:.2f}")
Total weekly pay: $1623.12
>>>
