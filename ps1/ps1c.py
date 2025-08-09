"""
This program calculates the best savings rate to achieve a down payment 
of a $1M house in 36 months, as a function of a starting salary, 
using a bisection search. 

It assumes the following:
1. Your semi_annual raise is .07 (7%)
2. Your investments have an annual return of 0.04 (4%)
3. The down payment is 0.25 (25%)
4. The cost of the house that you are saving for is $1M

The user inputs the starting salary, and the best saving rate is returned. 
The number ot steps in the bisection search is also listed. 

"""
# Variables from user
starting_salary = float(input("Enter the starting salary: "))


# Given variables
r = .04
down_payment = 250000   #25% of 1M
current_savings = 0
epsilon = 100

# Initialize variables
num_guess = 0
month_count = 0
low = 0.0    #Save nothing each month
high = 10000.0  #Save 100% each month

# To find max amount saved: 
annual_salary = starting_salary
monthly_salary = annual_salary / 12
max_savings = monthly_salary*36


while abs(current_savings - down_payment) >= epsilon and max_savings > down_payment:
    # Initialize values for each guess:
    current_savings = 0
    month_count = 0
    guess = (high + low)//2.0
    portion_saved = guess/10000   #Converting to a decimal percentage
    
    annual_salary = starting_salary
    monthly_salary = annual_salary / 12
    monthly_savings = monthly_salary*portion_saved

    #Calculate the amount earned in 36 months with each guess
    while month_count < 36:
        current_savings = current_savings + (current_savings*(r/12)) + monthly_savings
        month_count += 1
    
        #Apply raise every six months:
        if month_count % 6 == 0:
            annual_salary = annual_salary * (1.07)  #semi_annual_raise is 7%
            monthly_salary = annual_salary / 12
            monthly_savings = monthly_salary*portion_saved
           
    #Adjust guess
    if current_savings < down_payment:  
        # look only in upper half search space
        low = guess
    elif current_savings > down_payment:
        # look only in lower half search space
        high = guess

    num_guess += 1
        
# Print output:
if max_savings < down_payment:
    print("It is not possible to pay the down payment in three years.")
else: 
    print("Best savings rate:", portion_saved)
    print("Steps in bisection search:", num_guess)




