score = int(input("What's your credit score? "))

if score < 300 or score > 850:
    print("Invalid score.")
elif score >= 750:
    print("Excellent - Loan Approved. Interest rate: Low")
elif score >= 700:
    print("Good - Loan Approved with Review. Interest rate: Low")
elif score >= 600:
    print("Fair - Loan Conditional. Seek credit improvement.")
else:
    print("Poor - Loan Denied. Seek credit improvement.")