def even_occuring_element(arr):
    """Returns the even occuring element within a list of integers"""
    """Test like so: even_occuring_element([2,3,4,5,6,2,11])"""

    dict = {}
    for num in arr:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    for num in dict:
        if not dict[num] & 1: # bitwise check for parity.
            return num
