# 4.	Реализовать алгоритм Кнута-Морриса-Пратта для поиска по образцу
def compute_prefix_function(pattern):
    """Вычисление префикс-функции для шаблона."""
    n = len(pattern)
    prefix = [0] * n
    j = 0  # Длина текущего совпадающего префикса

    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]  # Возврат к предыдущему наибольшему префиксу

        if pattern[i] == pattern[j]:
            j += 1

        prefix[i] = j

    return prefix

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
