name=input("enter your name")
h=input("enter your height(m2):")
w=input("enter your Weight(Kg):")

if (h == "" or h == " ") or (w=='' or w==" "):
    print("Please enter the values!!!")
elif  float(h)<=0 or float(w)<=0 :
    print("your bmi couldnot be calculated")
else:
    bmi=float(w)/(float(h)**2)
    if not name:
        name="anonymous"
    if bmi < 18.5:
        print(f'oh! {name} you are "Underweight" with BMI of {bmi}')
    elif bmi>18.5 or bmi<24.9:
        print(f'oh! {name} you are "Normal weight" with BMI of {bmi}')
    else:
        print(f'oh! {name} you are "Overweight" with BMI of {bmi}')
        