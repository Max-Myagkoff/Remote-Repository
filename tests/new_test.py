from bubble_sort.py import bubble_sort
def test_bubble_sort():
    numbers = [64, 34, 25, 12, 22, 11, 90]
    sorted_numbers = bubble_sort(numbers)
    assert sorted_numbers == [90,64, 34, 25, 22, 12, 11]
