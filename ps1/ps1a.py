## 6.100A PSet 1: Part A
## Name: An Trung Dang
## Time Spent: 0:30
## Collaborators: None

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25 # percentage of the total cost needed for a down payment
amount_saved = 0            # amount that you have saved thus far
r = 0.05                    # annual rate of return
months = 0                  # number of months required to save for the down payment

cost_of_down_payment = cost_of_dream_home * portion_down_payment
monthly_salary = yearly_salary / 12
monthly_saved = monthly_salary * portion_saved

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved <= cost_of_down_payment:
    amount_saved += amount_saved * (r / 12)
    amount_saved += monthly_saved
    months += 1

print(f"Number of months: {months}")

