from Mypackage import myModule

def test_top_n():
    '''
    make sure top_n works correctly
    '''

    assert myModule.top_n([8,7,4,3,2], 3) == [8,7,4], 'incorrect'
    assert myModule.top_n([10,6,9,4,1], 4) == [10,9,6,4], 'incorrect'
    assert myModule.top_n([1,7,98,100,70], 3) == [100,98,70], 'incorrect'