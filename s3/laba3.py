def find_numbers(x):
    results = set()  # Используем множество, чтобы избежать дубликатов
    limit = x
    
    # Проходим по возможным значениям для K, L, M
    K = 0
    while 3**K <= limit: #перебор всех степеней
        L = 0
        while 3**K * 5**L <= limit:
            M = 0
            while 3**K * 5**L * 7**M <= limit:
                results.add(3**K * 5**L * 7**M)
                M += 1
            L += 1
        K += 1
    
    # Преобразуем множество в отсортированный список и возвращаем
    return sorted(results)

# Пример использования
x = int(input("Введите число: "))
result = find_numbers(x)
print(result)
