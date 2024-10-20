#Program to Check Leap Year

def leap_year(num):
    return (num%4 == 0 and num%100 != 0) or (num%400 == 0)
num = int(input("enter the year to check:"))
if leap_year(num):
    print(f" the {num} is leap year")
else:
    print(f" the {num} is not a leap year")

    
#Program to Find the Largest Among Three Numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number is", largest)
