
def build_fsm(pattern):
    """Построение конечного автомата для шаблона."""
    m = len(pattern)
    alphabet = set(pattern)
    fsm = [{char: 0 for char in alphabet} for _ in range(m + 1)]

    # Инициализация начального состояния
    for char in alphabet:
        if char == pattern[0]:
            fsm[0][char] = 1

    # Построение автомата
    longest_prefix = 0
    for state in range(1, m):
        for char in alphabet:
            fsm[state][char] = fsm[longest_prefix][char]

        fsm[state][pattern[state]] = state + 1
        longest_prefix = fsm[longest_prefix][pattern[state]]

    return fsm

def automaton_search(text, pattern):
    """Поиск всех вхождений pattern в text с использованием конечного автомата."""
    if not pattern or not text:
        return []

    fsm = build_fsm(pattern)
    m = len(pattern)
    state = 0
    result = []

    for i, char in enumerate(text):
        if char in fsm[state]:
            state = fsm[state][char]
        else:
            state = 0

        if state == m:
            result.append(i - m + 1)

    return result

if __name__ == "__main__":
    text = input("Введите текст: ")
    pattern = input("Введите образец для поиска: ")

    matches = automaton_search(text, pattern)

    if matches:
        print("Образец найден на позициях:", matches)
    else:
        print("Образец не найден")
