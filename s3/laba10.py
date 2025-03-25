def merge_sort(A):
    # Базовый случай: если массив длиной 1 или 0, он уже отсортирован
    if len(A) <= 1:
        return A
    
    # Разделяем массив на две части
    middle = len(A) // 2
    L = merge_sort(A[:middle])  # Левая часть
    R = merge_sort(A[middle:])  # Правая часть
    
    # Объединяем две отсортированные части
    C = []
    i = j = 0
    
    # Пока в обеих частях есть элементы
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            C.append(L[i])
            i += 1
        else:
            C.append(R[j])
            j += 1
    
    # Добавляем оставшиеся элементы из левой части, если есть
    C.extend(L[i:])
    
    # Добавляем оставшиеся элементы из правой части, если есть
    C.extend(R[j:])
    
    return C


arr = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
sorted_arr = merge_sort(arr)
print("Отсортированная последовательность:")
print(sorted_arr)