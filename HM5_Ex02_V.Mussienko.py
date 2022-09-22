
def input_values():
    try:
        pre_values = input('''\nВведите длины сторон выпуклого четырехугольника через запятой,\nа в конце значение одного угла в формате: 23,43,23,43,90 >>> ''').split(',')
        values = [int(value) for value in pre_values]

        return values
    
    except Exception as e:
        return e
        
def s_rectangle(a, b):
    s = a * b

    print(f'\nПлощадь вашего прямоугольника равно к {s}!\n')  


def checking(values):
    try:
        num_values = len(values)
        angle = values.pop()

        if num_values == 5 and angle == 90:
            el_values = set(values)
            count_el = len(el_values)

            if count_el == 2:
                a = el_values.pop()
                b = el_values.pop()

                s_rectangle(a, b)

            elif count_el == 1:
                print(f'\nЭто геометрическая фигура является "квадратом" со сторонами равные на {el_values.pop()}!\n')
    
        else:
            print('''\n(!) Этот фигура не является "прямоугольником",
            или же вы неправильно ввели данных.

            Убедитесь в правильности введенных данных и перезапустите программу*\n''')
        
    except Exception as e:
        return e

            
def main():
    values = input_values()
    checking(values)


if __name__ == '__main__':
    main()
