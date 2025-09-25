# input statements
salary = float(input('What is your salary? '))
numDependents = float(input('How many dependants do you have? '))

# calculate taxes here
stateTax = float(salary * 0.065)
federalTax = float(salary * .28)
dependantDeduction = float(salary * (numDependents * .025))
totalWithholding = float(stateTax + federalTax +dependantDeduction)
takeHomePay = salary - totalWithholding

# output statements
print('State Tax: $' + str(stateTax))
print('Fedral Tax: $' + str(federalTax))
print('Dependant Deduction: $' + str(dependantDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))