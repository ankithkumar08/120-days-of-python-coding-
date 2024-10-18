#swaping without using a temporary variable

a = int(input("Enter the a value :"))
b = int(input("Enter the b value :"))
a = a+b
b = a-b
a = a-b
print("After swapping")
print("a =",a)
print("b =",b)


#swapping with using a temporary variable

x = input('Enter value of x: ')
y = input('Enter value of y: ')
temp = x
x = y
y = temp
print("After swapping")
print('x=',x)
print('y=',y)
