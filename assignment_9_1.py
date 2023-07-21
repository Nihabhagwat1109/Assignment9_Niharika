#Niharika
from assignment_9_2 import Add, Sub, Mul, Div, FloorDiv, Exponent, Mod
num1=int(input("enter first number"))
num2=int(input("enter second number"))

choice = int(input('Enter your choice: '))
if choice == 1:
    Add.add(num1,num2) 
elif choice == 2:
    Sub.sub(num1,num2) 
elif choice == 3:
    Mul.mul(num1,num2) 
elif choice == 4:
    Div.div(num1,num2) 
elif choice == 5:
    FloorDiv.floordiv(num1,num2) 
elif choice == 6:
    Exponent.expo(num1,num2) 
elif choice == 7:
    Mod.mod(num1,num2) 
else:
    print("Invalid choice")

#Niharika