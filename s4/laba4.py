# 4.Реализовать алгоритм Кнута-Морриса-Пратта для поиска по образцу
#Алгоритм Кнута-Морриса-Пратта (КМП) используется для поиска подстроки 
# в строке и работает за линейное время 
# Он использует префикс-функцию, чтобы избегать лишних сравнений.


def compute_prefix_function(pattern):
    """Вычисление префикс-функции для шаблона."""
    n = len(pattern)
    prefix = [0] * n #массив, где prefix[i] хранит длину наибольшего собственного префикса, 
    #который также является суффиксом подстроки pattern[:i+1].
    j = 0  # Длина текущего совпадающего префикса
    #Проходим по pattern (от i = 1 до n-1).
    #Если pattern[i] != pattern[j], уменьшаем j, переходя к предыдущему 
    # совпадению j = prefix[j - 1].
    #Если pattern[i] == pattern[j], увеличиваем j и записываем его в prefix[i].

 
    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]  # Возврат к предыдущему наибольшему префиксу

        if pattern[i] == pattern[j]:
            j += 1

        prefix[i] = j

    return prefix
#Вычисляем prefix для pattern.
#m — длина text, n — длина pattern.
#j = 0 — индекс в pattern, отслеживающий совпадения.
#Основной алгоритм:
#Проходим text от i = 0 до m-1.
#Если text[i] != pattern[j], уменьшаем j, используя prefix[j - 1].
#Если text[i] == pattern[j], увеличиваем j.
#Если j == n, значит, нашли полное совпадение pattern в text.
#Записываем i - n + 1 (индекс первого символа).
#Уменьшаем j, чтобы продолжить поиск (используем prefix[j - 1]).


def kmp_search(text, pattern):
    """Поиск всех вхождений pattern в text с использованием алгоритма КМП."""
    prefix = compute_prefix_function(pattern)
    m, n = len(text), len(pattern)
    j = 0  # Текущая позиция в шаблоне
    result = []

    for i in range(m):
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]  # Возврат по префикс-функции

        if text[i] == pattern[j]:
            j += 1

        if j == n:  # Найдено совпадение
            result.append(i - n + 1)
            j = prefix[j - 1]  # Продолжить поиск с последнего совпадения

    return result

if __name__ == "__main__":
    text = input("Введите текст: ")
    pattern = input("Введите образец для поиска: ")

    matches = kmp_search(text, pattern)

    if matches:
        print("Образец найден на позициях:", matches)
    else:
        print("Образец не найден")
