string1 = input("Enter a string: ")
string2 = ("")
running = True
for i in string1:
  string2 = i + string2
print("Reverse string:", string2)