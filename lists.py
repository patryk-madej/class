numlist = list(range(1,51))

numlist2 = list(range(51,61))

numlist3 = numlist + numlist2

for num in numlist3:
    if num % 2 == 0:
        print(num, end = ", ") 

print('\n')

for num2 in numlist3:
    if num2 % 3 == 0:
        print(num2, end = ", ")
