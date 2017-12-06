wei = int(input("input ur weight(kg): "))
hei = int(input("input ur height(cm): "))
bmi = wei/((hei/100)**2)

if bmi < 16:
    print("your BMI: ", bmi)
    print("you are severely underweight")
elif bmi < 18.5:
    print("your BMI: ", bmi)
    print("you are underweight")
elif bmi < 25:
    print("your BMI: ", bmi)
    print("yoou are normal")
elif bmi < 30:
    print("your BMI: ", bmi)
    print("you are overweight")
else:
    print("your BMI: ", bmi)
    print("you are obese")
