"""
Created on Thu Aug  7 08:11:37 2025
@author: PamelaBrown

This program takes the following inputs:
1. Dream home cost
2. Amount of salary the user want's to save
3. The user's yearly salary
4. The user's semi-annual raise percentage.

Then it calculates the number of months it will take to save up for a 25% down payment. 
   
"""

#Get user inputs for annual salary, portion of salary to save, cost of dream home, and semi-annual raise
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#Initialize variables
current_savings = 0
portion_down_payment = .25
r = .04
month_count = 0

#Calcuate the month salary and monthly savings
monthly_salary = annual_salary/12
monthly_savings = monthly_salary*portion_saved

#Calculate the down payment needed
down_payment = total_cost * portion_down_payment

#Set up while loop to run until enough money is saved for a down payment
while current_savings < down_payment:
    current_savings = current_savings + (current_savings*(r/12)) + monthly_savings #current total + interest + montly savings
    
    month_count += 1
     
    #Apply raise every six months:
    if month_count % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12
        monthly_savings = monthly_salary*portion_saved
    
#Final print out of calculation
print("Number of months: ", month_count)