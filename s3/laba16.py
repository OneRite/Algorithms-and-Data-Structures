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


def non_recursive_pre_order(root):
    """Нерекурсивный прямой обход (pre-order) с использованием стека."""
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.value)

        # Сначала добавляем правого, затем левого ребенка
        # (чтобы левый был обработан раньше при pop)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result



input_data = "8(3(1,6(4,7)),10(,14(13,)))"  # Пример строки для дерева


tree_root = parse_tree(input_data)


pre_order_result = non_recursive_pre_order(tree_root)


print("Нерекурсивный прямой обход (pre-order):", ' '.join(map(str, pre_order_result)))
