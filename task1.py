first_two_years = 0.02
after_two_years = 0.04
loan_amount = float(input("Введіть суму кредиту: "))
years = int(input("Введіть строк погашення в роках: "))
months = years * 12
remaining_amount = loan_amount
for month in range(1, months + 1):
    if month <= 24:
        monthly_rate = first_two_years
    else:
        monthly_rate = after_two_years

    interest = remaining_amount * monthly_rate
    payment = remaining_amount + interest
    remaining_amount -= loan_amount / months
    print("{:<10} {:<20.2f} {:<20.2f}".format(month, payment, interest))
