import hashlib

# Функция для расчета хеша
def hash_function(key, table_size):
    hash_object = hashlib.md5(key.encode())
    return int(hash_object.hexdigest(), 16) % table_size

# Создание хеш-таблицы с цепочками
def create_hash_table(text, table_size):
    hash_table = [[] for _ in range(table_size)]
    for word in text.split():
        index = hash_function(word, table_size)
        hash_table[index].append(word)
    return hash_table

# Запись хеш-таблицы в файл
def write_table_to_file(hash_table, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i, chain in enumerate(hash_table):
            f.write(f"Index {i}: {chain}\n")

# Основной код
input_filename = 'input.txt'  # Укажите путь к вашему текстовому файлу
output_filename = 'hash_table_output.txt'
table_size = 10  # Укажите желаемый размер хеш-таблицы

# Чтение текста из файла
with open(input_filename, 'r', encoding='utf-8') as file:
    text = file.read()

# Создание и запись хеш-таблицы
hash_table = create_hash_table(text, table_size)
write_table_to_file(hash_table, output_filename)
