
# Создаем класс "Triangle"
class Triangle:
    # Иницализируем объекта
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Создаем метод "perimeter" который считает периметр данного треугольника.
    def perimeter(self):
        p = self.a + self.b + self.c

        print(f'Периметр треугольника со сторонами {self.a}, {self.b}, {self.c} равно к {p}. ')

    # Определяем, может ли существовать треугольник с данными нам сторонами и если да, то вызываем метод "perimeter".
    def exists(self):
        a = self.a
        b = self.b
        c = self.c
        if c > (a + b) or a > (b + c) or b > (a + c):
            print(f"Треугольник со сторонами {a}, {b}, {c} не может существовать в Евклидовом пространстве!")

        else:
            Triangle.perimeter(self)


# Создаем базу данных сторон треугольника с рандомными значениями.
def create_DB_triangles():
    from random import randint
    tri_es = []

    for i in range(20):
        tri = []
        for j in range(3):
            tri.append(randint(1, 50))

        tri_es.append(tri)

    return tri_es


def main():
    tri_es = create_DB_triangles()

    # Перебираем из базы данных элементов(треугольник) и создаем экземпляров класса "Triangle".
    for i in range(len(tri_es)):
        tri = tri_es[i]

        a = tri[0]
        b = tri[1]
        c = tri[2]

        Tr = Triangle(a, b, c)
        Tr.exists()


if __name__ == '__main__':
    main()
