"""
Created on Thu Aug  7 08:11:37 2025
@author: PamelaBrown
This program takes the inputs of dream home cost, amount of salary the user want's to save, and the user's yearly salary.
Then it calculates the number of months it will take to save up for a 25% down payment. 
   
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

current_savings = 0
portion_down_payment = .25
r = .04

month_count = 0
monthly_salary = annual_salary/12
monthly_savings = monthly_salary*portion_saved

down_payment = total_cost * portion_down_payment

while current_savings <= down_payment:
    current_savings = (current_savings + current_savings*(r/12) + monthly_savings)
    month_count += 1

print("Number of months: ", month_count)
