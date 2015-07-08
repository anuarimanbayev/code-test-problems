"""
Practice Makes Perfect!!!
"""

"""
Median!!!
The median is the middle number in a sorted sequence of numbers.

Finding the median of [7,12,3,1,6] would first consist of sorting the sequence
into [1,3,6,7,12] and then locating the middle value, which would be 6.

If you are given a sequence with an even number of elements, you must average
the two elements surrounding the middle.

For example, the median of the sequence [7,3,1,4] is 3.5, since the middle
elements after sorting the list are 3 and 4 and (3 + 4) / (2.0) is 3.5.

You can sort the sequence using the sorted() function, like so:
sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
"""
def median(old_list):
    # In Python 3: division / always returns a float. So, to get an integer, one has to use // or "floor division"
    # Floor division // rounds off to an integer ;)
    new_list = sorted(old_list)
    odd_avg = new_list[(len(new_list) - 1)//2]
    even_avg = (new_list[(len(new_list)//2)] + new_list[((len(new_list)//2) - 1)]) / 2.0
    if len(new_list) % 2 == 0:
        return even_avg
    else:
        return odd_avg

print(median([1, 2, 4]))
