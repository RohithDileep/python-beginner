name = "rohith"
print(type(name))
age = 19
age = float(age)
print(age)
#implicit
x = 4
y = 8.0
k = y / x
print(k)
#input functions
name = input("enter your name:")
age = input("enter your age:")
age = int(age)
age = age + 1
print(f"your name is{name}")
print(f"your age is {age}")

#areaofrectangle
l = float(input("enter the length :"))
b = float(input("enter the breadth :"))

area = l * b
print(f"the area is{area}cm^2")

#shoppingcart
item = input("enter the item :")
price = float(input("enter the price :"))
quantity = int(input("enter the quantity :"))
total = price * quantity
print(f"you have bought {quantity} {item}s")
print(f"the total amount is :{round(total,3)}")
