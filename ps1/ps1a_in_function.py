def part_a(yearly_salary, portion_saved, cost_of_dream_home):
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
	
	return months