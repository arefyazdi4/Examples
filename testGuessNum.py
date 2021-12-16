from random import seed
from random import randint

value = randint(0,99)
print(value)
gestNUmber = int(input("Enter your guess number: "))

while (gestNUmber is not value):
    if (gestNUmber<value):
        print("Upper")
    else:
        print("lower")
    
    gestNUmber = int(input("Enter your guess number: "))

print("ye you find it")