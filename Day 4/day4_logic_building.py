number = int(input("enter a number: "))

for i in range(1, number + 1):
    if i % 2 == 0:
        continue
    print(i)



number = int(input("enter a number: "))

total = 0
for i in range(1, number + 1):
    total = total + i

print(total)



number = int(input("enter a number: "))

count = 0
for i in range(1, number + 1):
    if i % 5 != 0:
        continue
    count = count + 1

print(count)




number = int(input("enter a number: "))

for i in range(1, number + 1):

    if i % 3 == 0 and i % 5 == 0:
        print("AI ML")

    elif i % 3 == 0:
        print("AL")

    elif i % 5 == 0:
        print("ML")
    
    else:
        print(i)



number = int(input("enter a number: "))

aiml_count = 0
ai_count = 0
ml_count = 0
for i in range(1, number + 1):
    if i % 15 == 0:
        aiml_count = aiml_count + 1
        print("AI ML count:", aiml_count)

    elif i % 3 == 0:
        ai_count = ai_count + 1
        print("AI:", ai_count)
    
    elif i % 5 == 0:
        ml_count = ml_count + 1
        print("ML:", ml_count)

    else:
        print(i)

print("/nFinal Counts:")
print("AI:", ai_count)
print("ML:", ml_count)
print("AI ML:", aiml_count)



number = int(input("enter a number: "))

if number <= 1:
    print("NOT PRIME")

else:
    is_prime = True

    for i in range(2,number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("PRIME")

    else:
        print("NOT PRIME")
        
 