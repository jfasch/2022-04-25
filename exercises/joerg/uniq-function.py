def unique(iterable):
    '''Returns a list that contains the elements from the ``iterable``
    parameter (which must be iterable), with all duplicates removed -
    while preserving the order of the element that were not removed.
    '''
    output_list = []
    have = set()
    
    for num in iterable:
        if num not in have:     # <---- HIER!!! SPEEEEEEED!!
            output_list.append(num)
            have.add(num)

    return output_list


input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]

unique_list = unique(input_list, [2,3,1,7,9,100])

for num in unique_list:
    print(num)


