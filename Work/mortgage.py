# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
standard_payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0

month = 0
while principal > 0:
    if extra_payment_start_month < month < extra_payment_end_month:
        payment = standard_payment + extra_payment
    else:
        payment = standard_payment

    if principal < payment:
        payment = principal * (1+rate/12)
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    month += 1
    print(f"Month: {month}; Paid: {round(total_paid, 2)}; Left: {round(principal, 2)}")

print('Total paid', total_paid, f"in {month} month")