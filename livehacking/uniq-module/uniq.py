import itertools


def unique(*iterable):
    '''Returns a list that contains the elements from the ``iterable``
    parameter (which could be arbitrarily many), with all duplicates
    removed - while preserving the order of the element that were not
    removed.

    '''
    output_list = []
    have = set()
    
    for num in itertools.chain(*iterable):
        if num not in have:     # <---- HIER!!! SPEEEEEEED!!
            output_list.append(num)
            have.add(num)

    return output_list
