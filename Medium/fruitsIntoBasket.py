from collections import Counter

def totalFruit(fruits):
    curr = 0
    fruitTypes, length, prev, maxFruits, types = Counter(), len(fruits), curr, 0, 0

    while curr < length:
        # Check if it is a new fruit and update the counter
        if fruitTypes[fruits[curr]] == 0: types += 1
        fruitTypes[fruits[curr]] += 1

        # We've encountered too many types, start reducing the counter
        while types > 2:
            fruitTypes[fruits[prev]] -= 1
            if fruitTypes[fruits[prev]] == 0: types -= 1
            prev += 1

        # Set maxFruits to the maximum window size
        maxFruits = max(maxFruits, curr - prev + 1)
        curr += 1
    return maxFruits
        

