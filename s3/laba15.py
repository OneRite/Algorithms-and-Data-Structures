class Node:
    #Класс для узла бинарного дерева.
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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
        # Найдем соответствующую закрывающую скобку
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


def pre_order(node):
    #Прямой обход (pre-order).
    if node is None:
        return []
    return [node.value] + pre_order(node.left) + pre_order(node.right)


def in_order(node):
    #Центральный обход (in-order).
    if node is None:
        return []
    return in_order(node.left) + [node.value] + in_order(node.right)


def post_order(node):
    #Концевой обход (post-order).
    if node is None:
        return []
    return post_order(node.left) + post_order(node.right) + [node.value]



input_data = "8(3(1,6(4,7)),10(,14(13,)))"  # Пример который в лабе (строки для дерева)


tree_root = parse_tree(input_data)


print("Прямой обход (pre-order):", pre_order(tree_root))
print("Центральный обход (in-order):", in_order(tree_root))
print("Концевой обход (post-order):", post_order(tree_root))
