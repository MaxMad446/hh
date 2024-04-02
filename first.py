import math

def circle_area(radius):
    return math.pi * radius**2

def triangle_area(side1, side2, side3):
    semiperimeter = (side1 + side2 + side3) / 2
    return math.sqrt(semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3))

def is_right_triangle(side1, side2, side3):
    sides = [side1, side2, side3]
    sides.sort()
    
    return sides[0]**2 + sides[1]**2 == sides[2]**2

if __name__ == "__main__":
    radius = 5
    print(f"Площадь круга с радиусом {radius}: {circle_area(radius)}")

    side1, side2, side3 = 3, 4, 5
    print(f"Площадь треугольника с сторонами {side1}, {side2}, {side3}: {triangle_area(side1, side2, side3)}")
    print(f"Является ли треугольник прямоугольным: {is_right_triangle(side1, side2, side3)}")


# Для добавления других фигур, например, прямоугольника, достаточно добавить соответствующую функцию и использовать её по аналогии с уже существующими.

# Для юнит-тестов можно использовать библиотеку unittest для написания тестов к функциям circle_area, triangle_area и is_right_triangle, чтобы убедиться в их корректной работе.
