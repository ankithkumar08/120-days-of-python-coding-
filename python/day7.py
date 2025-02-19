num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)



# Python program to find the factorial of a number provided by the user

def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return (x * factorial(x-1))

num = int(input("Enter a number: "))
result = factorial(num)
print("The factorial of", num, "is", result)
