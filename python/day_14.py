#Using the recursive methods

def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')
Dec = int(input("Enter the decimal number to convert to binary:"))
convertToBinary(Dec)
print()


#Using the Python's built-in functions!
         
Dec = int(input("Enter the decimal numver to convert into binary:"))
print(bin(Dec), "in binary.")
