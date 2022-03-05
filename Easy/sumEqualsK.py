import doctest

def subarraySum(nums, k):
    """
    Given an array of integers and a value k, return the number of 
    continuous subarrays of nums add up to k
    :param nums: List
    :param k: int
    :return: int

    >>> subarraySum([1, 1, 1], 2)
    2
    """

    count, total = 0, 0
    tracker = {0: 1}
    
    for i in range(len(nums)):
        total += nums[i];

        if (total - k) in tracker.keys():
            count += tracker[total - k]

        tracker[total] = (tracker.get(total,0) + 1)
    return count;

doctest.testmod()