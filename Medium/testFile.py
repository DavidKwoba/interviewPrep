"""
from collections import defaultdict
def totalFruit(fruits):
    fruitTypes = Counter()
            length = len(fruits)
            curr = 0
            prev, maxFruits, types = curr, 0, 0

            while curr < length:
                fruit = fruits[curr]
                # Check if it is a new fruit and update the counter
                if fruitTypes[fruit] == 0:
                    types += 1

                fruitTypes[fruit] += 1

                # We've encountered too many types, start reducing the counter
                while types > 2:
                    prevFruit = fruits[prev]
                    fruitTypes[prevFruit] -= 1
                    if fruitTypes[prevFruit] == 0:
                        types -= 1
                    prev += 1

                # Set maxFruits to the maximum window size
                maxFruits = max(maxFruits, curr - prev + 1)
                curr += 1
            return maxFruits

def testFruits(allFruits):
    keyList = list(allFruits)
    for i in range(len(keyList)):
        key = keyList[i]
        totalFruits = totalFruit(allFruits[key])
        if totalFruits == key: print("Test " + str(i) + " passed")
        else: print("Test " + str(i) + " failed")


al = {3: [1, 2, 1], 5: [0, 1, 2, 2, 2, 2], 4: [1, 2, 3, 2, 2]}
testFruits(al)

"""