p = int(input("Please give the the amount Rs "))
r = int(input("Please give the interest rate per annum "))/(12*100)
n = int(input("Please mention the time period in months "))

EMI = p * r * (1+r)**n / (1+r)**(n-1)

print(f"Your Monthly Installments would be RS {EMI}")