def CombSort(ls):
    n = len(ls) #длина списка
    step = n
    flag = True  # инициализируем flag
    while step > 1 or flag:
        if step > 1:
            step = int(step / 1.25)  # Уменьшаем step
        flag, i = False, 0
        while i + step < n:
            if ls[i] > ls[i + step]:
                ls[i], ls[i + step] = ls[i + step], ls[i]  # Меняем элементы местами
                flag = True  # Устанавливаем флаг, если был обмен
            i += 1  # Увеличиваем индекс на 1
    return ls

user_input = input("Введите числа через пробел: ")
arr = list(map(int, user_input.split()))  # Преобразуем строку в список чисел

# Сортируем массив
sorted_arr = CombSort(arr)

# Вывод результата
print("Отсортированный массив:", sorted_arr)
