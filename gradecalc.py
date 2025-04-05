numbers = []
n = 5
for i in range(n):
    num = int(input(f"Enter the mark subject {i+1} :"))
    numbers.append(num)
average = sum(numbers)/5
if average >= 90:
    print("A grade")
elif average >= 80:
    print("B grade")
elif average >= 70:
    print("C grade")
elif average >= 60:
    print("D grade")
else:
    print("YOU ARE FAILED")
