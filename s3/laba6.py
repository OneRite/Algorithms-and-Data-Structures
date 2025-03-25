def select_sort(A):
    for i in range(len(A) - 1):  # Проходим по каждому элементу
        min_index = i  # Считаем текущий элемент минимальным
        for k in range(i + 1, len(A)):  # Ищем минимальный элемент в оставшейся части
            if A[k] < A[min_index]:  # Если найден меньший элемент, обновляем min_index
                min_index = k
        A[i], A[min_index] = A[min_index], A[i]  # Меняем местами текущий элемент с найденным минимумом
    return A


user_input = input("Введите последовательность чисел, разделённых пробелами: ")
# Преобразование строки в список чисел
A = list(map(int, user_input.split()))
# Сортировка последовательности
sorted_A = select_sort(A)
print("Отсортированная последовательность:", sorted_A)
