def quick_sort(arr):
    # Базовый случай: если массив длиной 1 или меньше, он уже отсортирован
    if len(arr) <= 1:
        return arr
    
    # Выбор опорного элемента (обычно берём средний элемент)
    pivot = arr[len(arr) // 2]
    
    # Разделяем массив на три части: меньше опорного, равные  и больше элемента опорного
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Рекурсивно сортируем левую и правую части, а затем объединяем их с центральной частью
    return quick_sort(left) + middle + quick_sort(right)


arr = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
sorted_arr = quick_sort(arr)
print("Отсортированная последовательность:")
print(sorted_arr)
