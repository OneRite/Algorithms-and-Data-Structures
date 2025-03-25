import os

def external_sort(input_data, output_file, chunk_size=100, num_phases=3):
    # Этап 1: Разбиение входных данных на отсортированные чанки
    chunks = []
    index = 0
    while index < len(input_data):
        chunk = input_data[index:index+chunk_size]
        index += chunk_size
        chunk.sort()  # Сортируем чанк в памяти
        chunk_file = f"chunk_{len(chunks)}.txt"
        with open(chunk_file, 'w') as f:
            for number in chunk:
                f.write(f"{number}\n")
        chunks.append(chunk_file)

    # Этап 2: Многофазное слияние
    while len(chunks) > 1:
        # Применяем слияние чанков поэтапно
        next_chunks = []
        for i in range(0, len(chunks), num_phases):
            # Берем num_phases чанков для слияния
            files_to_merge = chunks[i:i+num_phases]
            next_chunk_file = f"merged_{len(next_chunks)}.txt"
            with open(next_chunk_file, 'w') as out_file:
                # Открываем все файлы для слияния
                files = [open(chunk, 'r') for chunk in files_to_merge]
                numbers = [int(file.readline().strip()) if file else float('inf') for file in files]

                while files:
                    # Находим минимальное число среди текущих элементов в каждом файле
                    min_index = numbers.index(min(numbers))
                    out_file.write(f"{numbers[min_index]}\n")
                    # Читаем следующий элемент из того же файла
                    line = files[min_index].readline().strip()
                    if line:
                        numbers[min_index] = int(line)
                    else:
                        files[min_index].close()
                        files_to_merge[min_index] = None
                        numbers[min_index] = float('inf')  

            # Удаляем временные файлы после слияния
            for file in files_to_merge:
                if file:
                    os.remove(file)

            next_chunks.append(next_chunk_file)

        chunks = next_chunks  # Переходим ко второму этапу слияния

    # Записываем окончательный отсортированный результат в выходной файл
    final_chunk = chunks[0]
    with open(final_chunk, 'r') as f, open(output_file, 'w') as out_file:
        for line in f:
            out_file.write(line)
    
    # Удаляем последний временный файл
    os.remove(final_chunk)


input_data = input("Введите числа через пробел для сортировки: ").split()
input_data = [int(num) for num in input_data]  # Преобразуем строки в числа

output_file = "sorted_numbers.txt"  
external_sort(input_data, output_file, chunk_size=100, num_phases=3)
print(f"Отсортированные числа сохранены в файл {output_file}")
