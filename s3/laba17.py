class Node:
    #Класс для узла бинарного дерева.
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def parse_tree(data):
    #Рекурсивный парсер линейно-скобочной записи.
    if not data:
        return None

    # Получаем значение корня
    value = ''
    i = 0
    while i < len(data) and data[i].isdigit():
        value += data[i]
        i += 1

    root = Node(int(value))  # Создаем корневой узел

    # Если осталась скобочная часть, обрабатываем её
    if i < len(data) and data[i] == '(':
        balance = 0
        start = i
        for j in range(i, len(data)):
            if data[j] == '(':
                balance += 1
            elif data[j] == ')':
                balance -= 1
            if balance == 0:
                # Разбиваем строку на левое и правое поддерево
                left_subtree = data[start + 1:j]
                right_subtree = data[j + 2:-1] if j + 2 < len(data) - 1 else ''
                root.left = parse_tree(left_subtree)
                root.right = parse_tree(right_subtree)
                break

    return root


def tree_to_string(root):
    #Преобразует дерево в линейно-скобочную запись
    if not root:
        return ''
    left = tree_to_string(root.left)
    right = tree_to_string(root.right)
    if left or right:
        return f"{root.value}({left},{right})"
    return str(root.value)


def insert(root, value):
    #Вставка элемента в бинарное дерево поиска
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def find_min(node):
    #Находит узел с минимальным значением
    while node.left:
        node = node.left
    return node


def delete(root, value):
    #Удаление элемента из бинарного дерева поиска
    if root is None:
        return root

    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        # Узел найден
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Узел с двумя детьми: заменяем на наименьший в правом поддереве
        min_larger_node = find_min(root.right)
        root.value = min_larger_node.value
        root.right = delete(root.right, min_larger_node.value)

    return root


def search(root, value):
    #Поиск элемента в бинарном дереве поиска
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)


def menu():
    #Меню для работы с деревом
    input_data = input("Введите дерево в линейно-скобочной записи: ")
    root = parse_tree(input_data)

    while True:
        print("\nМеню:")
        print("1. Поиск вершины")
        print("2. Добавление вершины")
        print("3. Удаление вершины")
        print("4. Вывод дерева")
        print("5. Выход")
        choice = input("Выберите опцию: ")

        if choice == '1':
            value = int(input("Введите значение для поиска: "))
            node = search(root, value)
            if node:
                print(f"Вершина {value} найдена.")
            else:
                print(f"Вершина {value} не найдена.")
        elif choice == '2':
            value = int(input("Введите значение для добавления: "))
            root = insert(root, value)
            print(f"Вершина {value} добавлена.")
        elif choice == '3':
            value = int(input("Введите значение для удаления: "))
            root = delete(root, value)
            print(f"Вершина {value} удалена.")
        elif choice == '4':
            print("Дерево в линейно-скобочной записи:", tree_to_string(root))
        elif choice == '5':
            print("Выход. Дерево:")
            print(tree_to_string(root))
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


# Запуск программмы
if __name__ == "__main__":
    menu()
