def shell_sort(data: list[int]) -> list[int]:
    last_index = len(data)
    step = len(data)//2
    while step > 0:
        for i in range(step, last_index, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - step
        step //= 2
    return data

# Получаем список чисел от пользователя
user_input = input("Введите последовательность чисел через пробел: ")
data = list(map(int, user_input.split()))

# Сортируем список
sorted_data = shell_sort(data)

# Выводим отсортированный список
print("Отсортированный список:", sorted_data)
