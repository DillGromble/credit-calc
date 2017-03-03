# retrieve user input
initial_balance = float(input(
        "Enter the outstanding balance on your credit card:\n>>> "))
annual_interest = float(input(
        "Enter the annual credit card interest rate as a decimal:\n>>> "))

# initialize variables
monthly_interest = annual_interest / 12
balance = initial_balance
lower_bound = balance / 12
upper_bound = (balance * (1 + monthly_interest) ** 12) / 12


while True:

    # reset variables
    balance = initial_balance
    payment = (upper_bound + lower_bound) / 2

    for month in range(1, 13):
        balance = round(balance * (1 + monthly_interest) - payment, 2)
        if balance <= 0:
            break

    # test margin and if successful, round up to closet cent and recalc and break
    if upper_bound - lower_bound < 0.004999:
        payment += 0.005
        balance = initial_balance
        for month in range(1, 13):
            balance = round(balance * (1 + monthly_interest) - payment, 2)
        break

    # paying too little
    elif balance > 0:
        lower_bound = payment
    # paying too much
    else:
        upper_bound = payment


print("\n\nRESULT")
print("Monthly payment to pay off debt in 1 year: $", round(payment, 2))
print("Number of months needed: ", month)
print("Ending Balance: $", round(balance, 2))
