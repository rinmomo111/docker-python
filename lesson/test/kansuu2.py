from unittest import result


def calc_square(side):
    return side * side
result = calc_square(side=100)
print(result)

def calc_tri(bottom,height):
    return bottom * height / 2
result = calc_tri(100,50)
print(result)

# default 設定できる（引数を空にしてもエラーにならない）
def calc_trapezium(top=100,bottom=200,height=50):
    return (top + bottom) * height
result = calc_trapezium()
print(result)


