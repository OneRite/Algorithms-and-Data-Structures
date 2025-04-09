#7.	Задача о самом большом подмассиве: поиск непрерывного 
# подмассива в одномерном массиве чисел с наибольшей суммой.
#(алгоритм Кадана)
def max_subarray_sum(arr):
    if not arr:
        return 0  # или float('-inf'), если нужно возвращать минимально возможное значение

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Пример использования
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(array)
print("Максимальная сумма подмассива:", result)
