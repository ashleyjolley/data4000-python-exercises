def get_tax_bracket(income):
    if income < 0:
        return "Invalid income."
    elif income < 50000:
        return "Low (10%)"
    elif income < 100000:
        return "Medium (20%)"
    else:
        return "High (30%)"


income = float(input("What's your annual income? "))

bracket = get_tax_bracket(income)

if income < 0:
    print(f"Your bracket: {bracket}")
elif income < 50000:
    tax = income * 0.10
    print(f"Your bracket: {bracket}. Estimated tax: ${tax:,.2f}")
elif income < 100000:
    tax = income * 0.20
    print(f"Your bracket: {bracket}. Estimated tax: ${tax:,.2f}")
else:
    tax = income * 0.30
    print(f"Your bracket: {bracket}. Estimated tax: ${tax:,.2f}")