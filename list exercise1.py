# num=[1,2,3,4,5,6,7]
# num.pop(4)
# print(num)


def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
        return square
    num = list(range(1,11))
    print(square_list(num))