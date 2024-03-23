# ( 1 = + ) ( 2 = - ) ( 3 = * ) ( 4 = / )

import random

num1 = int(input("number 1 - "))
num2 = int(input("number 2 - "))
num3 = int(input("number 3 - "))
list1 = (1,2,3,4)
math = random.choice(list1)
print("calculation...")
print(" ")
print("calculation...")
print(" ")
print("calculation...")
print(" ")
if num3 == 0:
    num3 = 1
if num2 == 0:
    num2 = 1
if num1 == 0:
        num1 = 1
if math == 1:
    print(num1 + num2 + num3)
elif math == 2:
    print(num1 - num2 - num3)
elif math == 3:
    print(num1 * num2 * num3)
elif math == 4:
    print(num1 / num2 / num3)


