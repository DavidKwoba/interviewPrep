def move_zeros_to_left(A):
    # num checks the number of zeroes already added
    num = 0
    index = 0
    length = len(A)

    while length > 0:
        num1 = A[index]
        if num1 == 0:
            A.pop(index)
            A.insert(num, num1)
            num += 1
        length -= 1
        index += 1


v = [1, 10, 20, 0, 59, 63, 0, 88, 0]
print("Original Array:", v)

move_zeros_to_left(v)

print("After Moving Zeroes to Left: ", v)
