def talkingcalculator():
    number1 = float(input("What's the width: "))
    number2 = float(input("What's the hight: "))

    question = input("float or integer? ")

    if question == 'float':
        area = float(number1 * number2)
        perimeter = float(number1 * 2 + number2 * 2)
        print('area:',area,'perimeter:',perimeter)

    elif question == 'integer':
        area = int(round(number1 * number2))                 #first version: area = int(number1 * number2) 
        perimeter = int(round(number1 * 2 + number2 * 2))    #int conversion will not round correctly, but strip decimals, so round downs)
        print('area:',area,'perimeter:',perimeter)          

    else:
        print('try again')

talkingcalculator()
