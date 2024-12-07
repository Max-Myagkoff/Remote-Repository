def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 1
    
def test_bubble_sort():
    numbers = [64, 34, 25, 12, 22, 11, 90]
    sorted_numbers = bubble_sort(numbers)
    assert sorted_numbers == [90,64, 34, 25, 22, 12, 11]
