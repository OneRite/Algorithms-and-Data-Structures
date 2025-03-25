def insertion_sort(arr):
    for i in range(1, len(arr)): #начинаем с элемента с индексом 1
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key


user_input = input("Введите числа, разделенные пробелами: ")

numbers = list(map(int, user_input.split())) # Преобразование строки в список чисел


insertion_sort(numbers)
print("Отсортированная последовательность:", numbers)
