rows = int(input("Enter number of rows: "))

for i in range(rows):
        print("*"*(i+1))

n = rows
for i in range(n):
    print(" " * (n-i-1) + "*" *(2*i+1))

print()

n = rows
for i in range(n-2,-1,-1):
    print(" " * (n-i-1) + "*" *(2*i+1))

