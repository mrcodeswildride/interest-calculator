print()

principal = float(input("Enter the principal: $"))
apr = float(input("Enter the APR: "))
num_years = int(input("Enter years to pay off loan: "))

decimal = apr / 100
yearly_interest = principal * decimal
total_interest = yearly_interest * num_years
monthly_payment = yearly_interest / 12

print(f"\nYearly interest: ${yearly_interest:,.2f}")
print(f"Total interest:  ${total_interest:,.2f}")
print(f"Monthly payment: ${monthly_payment:,.2f}")
