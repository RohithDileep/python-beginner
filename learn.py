#while loop
number = 100
while number > 0:
    print(number)
    number //= 2


#for loop
count = 0
for number in range(1,10):
    if number%2 == 0:
        count+=1
        print(number)
print(f"their is {count} even number")
