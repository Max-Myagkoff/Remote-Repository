from bubble_sort_to_test import bubble_sort
def test_bubble_sort():
    numbers = [64, 34, 25, 12, 22, 11, 90]
    sorted_numbers = bubble_sort(numbers)
    answer = [11,12,22,25,34,64,90]
    assert sorted_numbers == answer
