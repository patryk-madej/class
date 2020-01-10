import random

yellowpages = {}

for x in range (0,20):
    first_names=('John','Andy','Joe','Bob','Dave','Steve','Tom')
    last_names=('Johnson','Smith','Williams','Soup','Screen','Desk','Cloud')
    names = random.choice(first_names)+" "+random.choice(last_names)                      #old version " ".join( ----- for _ in range(20))

    num = random.randint(100000000,999999999)
    number = '7' + str(num)

    yellowpages[names]=number


print(yellowpages)
