# 6.Реализация алгоритма Рабина-Карпа для поиска подстроки в строке
#Рабин-Карп — это алгоритм, основанный на хэшировании. 
# Вместо посимвольного сравнения он сначала вычисляет хэш-значение 
# для подстроки и затем сравнивает только хэши. Если хэши совпадают, 
# выполняется дополнительная проверка, так как разные строки могут иметь 
# одинаковый хэш (коллизии).
#Преимущества алгоритма:
#Быстрее на множественных поисках (например, поиск нескольких слов).
#Можно адаптировать для поиска по множеству шаблонов.



def rabin_karp_search(text, pattern):
    """Поиск всех вхождений pattern в text с использованием алгоритма Рабина-Карпа."""
    m = len(pattern)
    n = len(text)
    if m == 0 or n == 0 or m > n: 
        #Если pattern или text пусты, или pattern длиннее text, 
        #возвращаем пустой список.


        return []

    # Параметры для хэш-функции
    base = 256  # Основание (количество символов в алфавите)
    prime = 101  # Простое число для вычисления хэша

    # Вычисление хэша для шаблона и первого окна текста
    # pattern_hash — хэш для pattern.
    #window_hash — хэш для первого окна text.
    #h = base^(m-1) % prime используется для удаления старого символа при перерасчете.
    pattern_hash = 0
    window_hash = 0
    h = 1

    # Значение base^(m-1) % prime
    for i in range(m - 1):
        h = (h * base) % prime

    for i in range(m): #читаем хэш шаблона и первого окна text.
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        window_hash = (base * window_hash + ord(text[i])) % prime

    result = []

    # Поиск шаблона в тексте
    for i in range(n - m + 1): #Скользящее окно по text.
        # Если хэши совпали, проверяем строку посимвольно
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                result.append(i)

        # Пересчитываем хэш для следующего окна
        if i < n - m:
            window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % prime

            # В случае отрицательного хэша делаем его положительным
            if window_hash < 0:
                window_hash += prime

    return result

if __name__ == "__main__":
    text = input("Введите текст: ")
    pattern = input("Введите образец для поиска: ")

    matches = rabin_karp_search(text, pattern)

    if matches:
        print("Образец найден на позициях:", matches)
    else:
        print("Образец не найден")
