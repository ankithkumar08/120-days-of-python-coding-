#using lambda function

my_list = [12, 65, 54, 39, 102, 339, 221]
result = list(filter(lambda x: (x % 13 == 0),my_list))
print("Number divisible by 13 are ",result)

#using enumerate

my_list = [12, 65, 54, 39, 102, 339, 221]
x = int(input("Enter the number to check divisible :"))
list2 = []
for index, val in enumerate(my_list):
    if val % x == 0:
        list2.append(val)
print(f"Number divisible by {x} are :",list2)
