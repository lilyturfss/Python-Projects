# BMI CALC

print("**BMI Calculator** - I decided to do something simple this time - Karen Ruiz")
print("")

metric = input("Metric or imperial: ")
while metric.lower() != "metric" and metric.lower() != "imperial":
    print("That is not a valid answer, try again.")
    metric = input("Metric or imperial: ")

while True:
    if metric.lower() == "metric":
            try:
                height = float(input("Input your height in meters: "))
                weight = float(input("Input your weight in kgs: "))
                bmi = weight/height**2
                break
            except:
                print("Those are not valid inputs, try again.")
    elif metric.lower() == "imperial":
            try:
                height = float(input("Input your height in inches: "))
                weight = float(input("Input your weight in lbs: "))
                bmi = 703*weight/height**2
                break
            except:
                print("Those are not valid inputs, try again.")
if bmi <= 18:
    status = "underweight"
elif bmi > 18 and bmi < 25:
    status = "healthy" 
elif bmi > 25 and bmi < 30:
    status = "overweight"
elif bmi > 30 and bmi < 40:
    status = "obese"
else:
    status = "morbidly obese"

print("Your BMI is", bmi, "and you are", status)
