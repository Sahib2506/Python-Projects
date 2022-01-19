print("Welcome to time left to reach 90 years of Age Calculator\n")

#Getting User Input for age
age = input("What is your current age? ")

age_as_int = int(age) # Converting datatype which is in string format

#Calculation Part
years_left= 90 - age_as_int
days = years_left * 365
weeks = years_left * 52
months = years_left * 12

#Final Output
print(f"\n You have {days} days, {weeks} weeks, and {months} months left.")






