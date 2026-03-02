name = "Hrusikesh"
age = 20
height = 5.8
is_student = True 

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
a = 10
b = 3

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b) # Floor division
print(a % b)  # Remainder 
print(a ** b) # Power


number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd") 



number = int(input("Enter a number: "))
if number % 10 == 0:
    print("Divisible by 5 and 2")
else:
    print("May be Divisible by 5 but not 2")



number = int(input("Enter anumber: "))
if number % 2 == 0 or number % 5 == 0:
    print("Yes")
else:
    print("No")



number = int(input("Entera number: "))
if number % 21 == 0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both 3 and 7")



number = int(input("Enter a number: "))
if number >= 10 and number <= 50:
    print("Yes")
else:
    print("No")



number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("First is greater")
elif num1 < num2:
    print("Second is greater")
else:
    print("Both are equal")



number = int(input("Enter a number: "))
if number % 15 == 0: 
    print("devisible by 3 and 5")
elif number % 3 == 0 and number % 5 != 0:
    print("Divisible by 3 but not 5")
else:
    print ("Not divisible by noth 3 and 5")