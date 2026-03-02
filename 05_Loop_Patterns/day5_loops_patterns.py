for i in range(1,51):
    if i % 17 == 0:
        break

    elif i % 3 == 0:
        continue

    else:
        print(i)




number = int(input("enter a number: "))

if number < 0:
    print("Factrial dose not exit for negative numbers")

else:
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i

    print("Factrial:", fact)





number = int(input("enter a number: "))

if number < 0:
    print("Factorial does not exist for negative numbers")

else:
    fact = 1
    i = 1

    while i <= number:
        fact = fact * i
        i += 1

    print("Factorial:", fact)






nummber = int(input("enter a number: "))

if number <= 1:
    print("Not a Prime")

else:
    is_prime = True

    for i in range(2,number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")|

    else:
        print("Not a Prime")





number = int(input("enter a number: "))

if number <= 1:
    print("NOT A PRIME")

else:
    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if  number % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("PRIME")

    else:
        print("NOT A PRIME")





for num in range(1,51):

    if num <= 1:
        continue

    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)

    
        


    



