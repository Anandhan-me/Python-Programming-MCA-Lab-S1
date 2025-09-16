age = int(input("enter the age of customer : "))
if age < 10 :
    print("Rate = 7 Rupees")
elif age >=10 and age<60 :
    print("Rate = 10 Rupees")
elif age >=60 and age<100 :
    print("Rate = 5 Rupees")
else :
    print("Something went wrong !!!")