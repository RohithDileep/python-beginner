operator=input("enter the operators(+,-,/,*):")
num1=float(input("enter the first  number:"))
num2=float(input("enter the second number:"))

if operator=="+":
   result=num1+num2
   print(round(result,2))
if operator =="-":
   result=num1-num2
   print(round(result,2))
if operator =="/":
   result=num1/num2
   print(round(result,2))
if operator =="*":
   result=num1 *num2
   print(round(result,2))
else:
    print(f"{operator} is a invalid operator")
