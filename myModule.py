def top_n (items, n):
    '''Return the top n items in an array, in desc order 
    Args:
        items (array): list or an array like object
        n (int): number of items to return
        
    Return 
            array: top n items in desc order
            
    Egs:
        >>> top_ n([8,3,2,4,7], 3)
        [8,7,4]
    '''

    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]: # if this item is bigger than the next item
                items[j], items[j+1] = items[j+1], items[j] # swop the two
    
    # get the last two items
    top_n = items[-n:]

    #rerutn in descending order
    return top_n[::-1]
