#Using String methods 

my_str =input("Enter the string  to check the palindrome:")
my_str = my_str.casefold()
rev_str = reversed(my_str) 
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")



#Using slicing 

my_str =input("Enter the string  to check the palindrome:")
my_str = my_str.casefold()
rev_str = my_str[::-1]  
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

#Methid3

s = input("Enter the string  to check the palindrome:")
S = ""
s = s.casefold()
for i in s:
    S=i+S
if S==s:
    print("given string is a palendrome")
else:
    print("the given string is not a palendrome")
