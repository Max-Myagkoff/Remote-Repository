def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n-i-1):
            # Меняем местами, если элемент найден больше, чем следующий
            if arr[j] > arr[j+1]:
              
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr



