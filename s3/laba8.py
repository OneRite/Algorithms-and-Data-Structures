def counting_sort(arr, exp):
    n = len(arr) #длина массива
    output = [0] * n  # результирующий массив ,уже отсорт эл
    count = [0] * 10  # вспомогательный массив для подсчета
    # Подсчитываем количество вхождений каждой цифры
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    # Изменяем count чтобы содержать актуальные индексы для вывода
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Формируем отсортированный массив
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    # Копируем отсортированный массив обратно в оригинальный
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Получаем максимальное число для определения количества разрядов
    max_num = max(arr)
    
    # Применяем сортировку подсчетом для каждого разряда
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Ввод последовательности чисел пользователем
arr = list(map(int, input("Введите последовательность неотрицательных чисел через пробел: ").split()))

radix_sort(arr)
print("Отсортированный массив:", arr)
