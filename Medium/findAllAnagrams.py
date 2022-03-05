import doctest
from collections import defaultdict

def findAnagrams(str1, str2):
    """
    Given two strings s and p, return an array of 
    all the start indices of p's anagrams in s.

    >>> findAnagrams("cbaebabacd", "abc")
    [0, 6]
    """

    tracker, result, str2Length, str1Length = defaultdict(int), [], len(str2), len(str1)

    # base case
    if str2Length > str1Length: return []

    # build hashmap
    for ch in str2: tracker[ch] += 1

    # initial full pass over the window
    for i in range(str2Length - 1):
        cur = str1[i]
        if cur in tracker: tracker[cur] -= 1

    # slide the window with stride 1
    for i in range(-1, str1Length - str2Length + 1):
        lastCur = str1[i]
        # Increase the corresponding counter in hashmap 
        # when the letter gets out of the window
        if i > -1 and lastCur in tracker:
            tracker[lastCur] += 1

        # Decrease the corresponding value in the hashmap when 
        # the letter gets in the window
        if i + str2Length < str1Length and str1[i + str2Length] in tracker:
            nextCh = str1[i + str2Length]
            tracker[nextCh] -= 1
            
        # check whether all the letters in the tracker have been encountered (anagram)
        if all(v == 0 for v in tracker.values()):
            index = i + 1
            result.append(index)

    return result

doctest.testmod()