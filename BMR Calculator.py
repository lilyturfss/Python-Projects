#Input/Output - BMR Calculator

print("Basal Metabolic Rate Calculator (BMR)")
print("Your BMR is basically your calorie expenditure by living.")

while True:
    gender = input("Are you female or male? ")
    if gender == "female" or gender == "male":
        break
    else:
        print("Please enter female or male.")

age = int(input("How old are you? (in years, no decimals) "))
height = int(input("How tall are you in centimeters? "))
weight = int(input("How much do you weigh in kilograms? "))

if gender == "female":
    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
else:
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

print("Your Basal Metabolic Rate (BMR) is:", bmr)