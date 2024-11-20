string = input("Enter a string: ")
words = [word.lower() for word in string.split()]
print(words)
words.sort()
print("The sorted words are:")
for word in words:
   print(word)
