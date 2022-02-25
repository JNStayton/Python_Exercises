def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    tracker = {}
    for num in nums:
        if tracker.get(num) == None:
            tracker[num] = nums.count(num)
    
    mode_val = max(tracker.values())

    return [key for key, value in tracker.items() if value == mode_val][0]
    


