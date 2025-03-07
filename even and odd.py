#task1 find even and odd numbers
number  = int(input('Enter the Number: '))

if number%2 == 0:
    print(number,'is an even number')
elif number%2 != 0:
    print(number,'is an odd number')
else:
    print('enter a valid number')