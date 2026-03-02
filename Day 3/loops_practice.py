for i in range(5):
    print(i)

    

for i in range(1,6):
    print(i)



number = int(input("enter a number: "))

for i in range(1, number + 1):
    print(i)



number = int(input("enter a number: "))

for i in range(number,0,-1):
    print(i)



number = int(input("enter a number: "))

total = 0

for i in range(1, number + 1):
    total = total + i

print(total)



number = int(input("enter a number: "))

total = 0

for i in range(2, number + 1,2):
    total = total + i

print(total)



number = int(input("enter a number: "))

total = 0

for i in range(1, number + 1,2):
    total = total + i

print(total)



number = int(input("enter a number: "))

for i in range(1,11):
    result = number * i
    print(number, "x", i, "=", result)



number = int(input("enter a number: "))

count = 0
for i in range (1, number + 1):
    count = count + 1

print(count)



number = int(input("enter a number: "))

for i in range(number,-1,-1):
    print(i)

print("done")



number = int(input("enter a number: "))

for i in range(number,-1,-1):
    if i % 2 == 0:
        print(i)



number = int(input("enter a number: "))

if number % 2 != 0:
    number = number - 1

for i in range(number,-1,-2):
    print(i)



number = int(input("enter a number: "))

for i in range(1, number + 1):
    if i % 3 != 0:
        print(i)



number = int(input("enter a number: "))

 for i in range(1, number + 1):
    if i % 3 == 0:
        continue
    print(i)