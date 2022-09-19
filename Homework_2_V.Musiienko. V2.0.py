num = int(input('Enter a number: '))

if num <= -500:
    print('The number is equal to or less than -500')
elif num <= -100:
    print('Equal to or less than -100 but greater than -500')
elif num < 0:
    print('Less than 0 but greater than -100')
elif num < 100:
    print('Equal to or greater than 0 but less than 100')
elif num <= 500:
    print('Equal to or greater than 100 but less than 500')
else:
    print('Equal to or greater than 500')
