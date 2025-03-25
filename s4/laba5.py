# Реализация алгоритма Бойера-Мура для поиска подстроки в строке

def boyer_moore_search(text, pattern):
    """Поиск всех вхождений pattern в text с использованием алгоритма Бойера-Мура."""
    m = len(pattern)
    n = len(text)

    if m == 0 or n == 0 or m > n:
        return []

    # Построение таблицы плохих символов
    bad_char = {char: m for char in set(text)}
    for i in range(m - 1):
        bad_char[pattern[i]] = m - 1 - i

    result = []
    shift = 0

    while shift <= n - m:
        j = m - 1

        # Проверка совпадения с конца шаблона
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            result.append(shift)
            shift += m  # Сдвиг на длину шаблона
        else:
            shift += bad_char.get(text[shift + m - 1], m)

    return result

if __name__ == "__main__":
    text = input("Введите текст: ")
    pattern = input("Введите образец для поиска: ")

    matches = boyer_moore_search(text, pattern)

    if matches:
        print("Образец найден на позициях:", matches)
    else:
        print("Образец не найден")
