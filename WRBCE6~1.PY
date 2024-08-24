

# Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-1lakh print k).
salary = int(input("Enter your salary: "))
HRA = 0.10 * salary
DA = 0.5 * salary
PF = 0.3 * salary
total_deduction = HRA - DA - PF
salary_after_deduction =salary -  total_deduction
if salary <= 100000:
    tax = 0
    print("K")
elif salary <= 1000000:
    tax = 0.10 * salary_after_deduction
elif salary <= 2000000:
    tax = 0.20 * salary_after_deduction
else:
    tax = 0.30 * salary_after_deduction
    hand_salary = salary_after_deduction - tax
    print(hand_salary)

