
def build_fsm(pattern):# Эта функция строит конечный автомат (FSM), 
    #который используется для поиска образца (pattern) в тексте. 
    """3.Реализовать алгоритм поиска по образцу с помощью конечного автомата"""
    m = len(pattern) # длина шаблона
    alphabet = set(pattern) # алфавит (уникальные символы шаблона)
    fsm = [{char: 0 for char in alphabet} for _ in range(m + 1)] #Создается список словарей, 
    #где каждый ключ — символ из алфавита, а значение — следующее состояние автомата.

    # Инициализация начального состояния
    # Если символ совпадает с первым символом образца, 
    # то при его встрече автомат переходит в состояние 1.
    for char in alphabet:
        if char == pattern[0]:
            fsm[0][char] = 1

    # Построение автомата
    # Проходим по всем состояниям state (от 1 до m-1).
    # Для каждого символа char копируем переходы из состояния longest_prefix.
    # Если текущий символ совпадает с символом образца, 
    # устанавливаем fsm[state][pattern[state]] = state + 1.
    #Обновляем longest_prefix (самая длинная граница образца, совпадающая с префиксом).
    longest_prefix = 0
    for state in range(1, m):
        for char in alphabet:
            fsm[state][char] = fsm[longest_prefix][char]

        fsm[state][pattern[state]] = state + 1
        longest_prefix = fsm[longest_prefix][pattern[state]]

    return fsm

def automaton_search(text, pattern):
    #Эта функция ищет все вхождения pattern в 
    # text с использованием построенного конечного автомата.
    if not pattern or not text:
        return [] #если строка или списк пусто то возвращаем пустой список

    fsm = build_fsm(pattern) #построение автомата
    m = len(pattern) # определяем длину
    state = 0
    result = [] 
 
 #Проходим по всем символам текста.
 #Если символ есть в fsm[state], переходим в следующее состояние.
 #Если символ не соответствует, сбрасываем состояние в 0.
 #Если state == m, значит образец найден (достигнуто конечное состояние автомата).
 #Добавляем i - m + 1 в result, так как i указывает на последний символ найденного образца.
    for i, char in enumerate(text):
        if char in fsm[state]:
            state = fsm[state][char]
        else:
            state = 0

        if state == m:
            result.append(i - m + 1)

    return result  # return должен быть на одном уровне с for

if __name__ == "__main__":
    text = input("Введите текст: ")
    pattern = input("Введите образец для поиска: ")

    matches = automaton_search(text, pattern)

    if matches:
        print("Образец найден на позициях:", matches)
    else:
        print("Образец не найден")
