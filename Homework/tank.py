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
if math == 1:
    print(num1 + num2 + num3)
elif math == 2:
    print(num1 - num2 - num3)
elif math == 3:
    print(num1 * num2 * num3)
elif math == 4:
    print(num1 / num2 / num3)