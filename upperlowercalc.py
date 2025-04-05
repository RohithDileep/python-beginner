count1 = 0
count2 = 0
text = input("enter the string :")
for char in text:
    if char.isupper():
        count1+= 1
    elif char.islower():
        count2+= 1
print(f"Their are {count1} uppercase and {count2} lowercase")
