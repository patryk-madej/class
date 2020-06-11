'''
0 + 1 = 1
    1 + 1 = 2
        1 + 2 = 3
            2 + 3 = 5

0, 1, 1, 2, 3, 5, 8
'''
lst=[1,1]

def fib(lst,num):
    for i in range(num):
        fib=lst[-1]+lst[-2]
        lst.append(fib)
    return lst

print(fib(lst,10))

