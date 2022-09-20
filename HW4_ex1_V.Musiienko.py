import math

x1 = math.pi
def rad_to_degr(value, x1):
    result = (value * 180) / x1

    print(f'\n{value} радиан = {result} градус.\n')

def degr_to_rad(value, x1):
    result = (value * x1) / 180

    print(f'\n{value} градус = {result} радиан.\n')

def main():
    answer = float(input('''\nВыберите один из следующих вариантов (Введите номер варианта*):
    1) радианы в градусы(угол).
    2) градусы в радианы.\n >>> '''))

    if answer == 1:
        value = float(input('\nВведите знчение в радианах(Например: 6 ): >>> '))
        rad_to_degr(value, x1)

    elif answer == 2:
        value = float(input('\nВведите знчение в градусах(Например: 128.8 или 95 ): >>> '))
        degr_to_rad(value, x1)

    else:
        print('\n(!) Убедитесь в правильности введенных данных\n')


if __name__ == '__main__':
    main()
