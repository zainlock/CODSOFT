def calculate():

    number_1 = eval(input('Please enter the first number: '))
    number_2 = eval(input('Please enter the second number: '))
    operation = input('''
Please type in the math operation you would like to complete:
1 for addition (+)
2 for subtraction (-)
3 for multiplication (*)
4 for division (/)
''')
    if operation == '1':
        print('{} + {} = '.format(number_1, number_2),(number_1 + number_2))

    elif operation == '2':
        print('{} - {} = '.format(number_1, number_2),(number_1 - number_2))

    elif operation == '3':
        print('{} * {} = '.format(number_1, number_2),(number_1 * number_2))

    elif operation == '4':
        print('{} / {} = '.format(number_1, number_2),(number_1 / number_2))

    elif operation == '5':
        print('{} % {} = '.format(number_1, number_2),(number_1 % number_2))

    else:
        print('You have not typed a valid operator, please run the program again.')

    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()