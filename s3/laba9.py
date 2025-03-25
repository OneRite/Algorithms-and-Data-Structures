def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1  # левый = 2*i + 1
    right = 2 * i + 2  # правый = 2*i + 2

    # Проверяем, существует ли левый дочерний элемент больший, чем корень
    if left < n and arr[i] < arr[left]:
        largest = left

    # Проверяем, существует ли правый дочерний элемент больший, чем корень
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Заменяем корень, если нужно
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # свап

        # Применяем heapify к поддереву
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи один за другим
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # свап
        heapify(arr, i, 0)


arr = list(map(int, input("Введите последовательность чисел через пробел: ").split()))

# Сортируем массив
heapSort(arr)

print("Отсортированная последовательность:")
print(arr)
