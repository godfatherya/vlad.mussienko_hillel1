def rad_to_degr(value, pi):
    result = (value * 180) / pi

    print(f'\n{value} радиан = {result} градус.\n')

def degr_to_rad(value, pi):
    result = (value * pi) / 180

    print(f'\n{value} градус = {result} радиан.\n')


def main():
    answer = float(input('''\nВыберите одну из следующих вариантов (Введите номер варианта*):
    1) радианы в градусы(угол).
    2) градусы в радианы.\n >>> '''))

    pi = 22/7

    if answer == 1:
        value = float(input('\nВведите знчение в радианах(Например: 6 ): >>> '))
        rad_to_degr(value, pi)

    elif answer == 2:
        value = float(input('\nВведите знчение в градусах(Например: 128.8 или 95 ): >>> '))
        degr_to_rad(value, pi)

    else:
        print('\n(!) Убедитесь в правильности введенных данных и перезапустите программу*\n')


if __name__ == '__main__':
    main()
