"""
Practice Makes Perfect!!!
"""

"""
Remove Duplicates!!!
Write a function remove_duplicates that takes in a list and removes elements of
the list that are the same.

For example: remove_duplicates([1,1,2,2]) should return [1,2].
"""
def remove_duplicates(old_list):
    new_list = []
    
    for i in old_list:    
        if i not in new_list:
            new_list.append(i)
    return new_list

old_list = [4, 5, 5, 4]
print(old_list)
print(remove_duplicates(old_list))
