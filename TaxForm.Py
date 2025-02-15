>>> TAX_RATE = 0.20
>>> STANDARD_DEDUCTION = 10000.0
>>> DEPENDENT_DEDUCTION = 3000.0
>>> grossIncome = float(input("Enter the gross income: "))
Enter the gross income: 12345.67
>>> numDependents = int(input("Enter the number of dependents: "))
Enter the number of dependents: 1
>>> taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
>>> incomeTax = taxableIncome * TAX_RATE
>>> print("The income tax is $" + str(round(incomeTax, 2)))
The income tax is $-130.87
>>>
