import hashlib


class Node:
    #Узел связного списка для хранения данных в случае наложения
    def __init__(self, word):
        self.word = word
        self.next = None  # Указатель на следующий узел


class HashTable:
    #Хеш-таблица с наложением на основе связного списка
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Массив указателей на начало связных списков

    def hash_function(self, word):
        #Хеш-функция на основе SHA-256
        hash_object = hashlib.sha256(word.encode())
        return int(hash_object.hexdigest(), 16) % self.size

    def insert(self, word):
        #Вставка слова в хеш-таблицу
        hash_key = self.hash_function(word)
        if self.table[hash_key] is None:
            # Если в ячейке пусто, создаем новый узел
            self.table[hash_key] = Node(word)
        else:
            # Если коллизия, добавляем узел в конец связного списка
            current = self.table[hash_key]
            while current:
                if current.word == word:
                    return  # Слово уже есть в таблице, пропускаем
                if current.next is None:
                    break
                current = current.next
            current.next = Node(word)

    def __str__(self):
        #Форматированный вывод хеш-таблицы
        result = []
        for i, node in enumerate(self.table):
            chain = []
            current = node
            while current:
                chain.append(current.word)
                current = current.next
            if chain:
                result.append(f"{i}: {' -> '.join(chain)}")
        return "\n".join(result)


# Основная часть программы
input_file = "input.txt"      # Имя входного текстового файла
output_file = "output.txt"    # Имя файла для записи хеш-таблицы
table_size = 100              # Размер хеш-таблицы

# Чтение текста из файла
try:
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Очистка текста и разбиение на слова
    words = text.split()

    # Создание хеш-таблицы
    hash_table = HashTable(table_size)

    # Заполнение хеш-таблицы словами
    for word in words:
        hash_table.insert(word)

    # Запись хеш-таблицы в файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(hash_table))

    print(f"Хеш-таблица записана в файл {output_file}.")
except FileNotFoundError:
    print(f"Файл {input_file} не найден.")
except IOError as e:
    print(f"Ошибка при работе с файлами: {e}")
