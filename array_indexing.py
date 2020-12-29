class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def merge_intervals(v):
    # write your code here
    last_index = len(v) - 1
    num1 = v[0][0]
    num2 = v[last_index][1]
    result = [num1, num2]
    print(result)


v = [(1, 2), (4, 5), (7, 8)]
merge_intervals(v)
