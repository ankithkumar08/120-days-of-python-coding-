#Python Program to Display Powers of x Using Anonymous Function

x = int(input("Enter the number raised to power:"))
terms = int(input("How many terms? "))
# use anonymous function
result = list(map(lambda y: x** y, range(terms)))
print("The total terms are:",terms)
for i in range(terms):
   print(f"{x} raised to power",i,"is",result[i])
   
