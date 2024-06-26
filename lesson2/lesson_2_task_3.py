side = float(input('Введите сторону квадрата: '))
import math
def square(side):
    return math.ceil((side*side))
print(square(side))