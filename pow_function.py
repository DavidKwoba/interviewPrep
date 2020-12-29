def raise_num(base, power):
    result = base
    for i in range(power - 1):
        result = result * base
    print(result)


raise_num(2, 3)
