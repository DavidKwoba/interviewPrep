from collections import Counter

def totalFruit(fruits):
    curr = 0
    fruitTypes, length, prev, maxFruits, types = Counter(), len(fruits), curr, 0, 0

    while curr < length:
        fruit = fruits[curr]
        # Check if it is a new fruit and update the counter
        if fruitTypes[fruit] == 0: types += 1
        fruitTypes[fruit] += 1

        # We've encountered too many types, start reducing the counter
        while types > 2:
            prevFruit = fruits[prev]
            fruitTypes[prevFruit] -= 1
            if fruitTypes[prevFruit] == 0: types -= 1
            prev += 1

        # Set maxFruits to the maximum window size
        maxFruits = max(maxFruits, curr - prev + 1)
        curr += 1
    return maxFruits
        

