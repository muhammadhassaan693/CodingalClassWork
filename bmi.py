height=float(input("enter your height in cm "))
weight=float(input("enter your weight in kg "))
bmi=weight/((height/100)**2) #convert the height in to meaters and multiply it by itself  

if bmi <= 18.4:
    print("you are under weight")
elif 18.5 <= bmi<= 24.9:
    print("you are healthy")
elif 25.0 <= bmi<= 29.9:
    print("you are over weight")
elif 30.0 <= bmi<= 34.9:
    print("you are severely over weight")
elif 35.0 <= bmi<= 39.9:
    print("you are obese")  
else:
    print("you are severely obese")  