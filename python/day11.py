#Sum of natural numbers up to num

num =int(input("Enter the number to calculate sum of natural numbers up to :"))
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
