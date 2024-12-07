import bubble_sort
def test_bubble_sort():
    numbers = [64, 34, 25, 12, 22, 11, 90]
    sorted_numbers = bubble_sort(numbers)
    answer = [90,64, 34, 25, 22, 12, 11]
    assert sorted_numbers == answer
