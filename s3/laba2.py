def check_brackets(expression):
    # Проверка корректности скобок
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

def check_division_by_zero(expression):
    # Проверка на деление на ноль
    parts = expression.split('/')
    for part in parts[1:]:
        part = part.lstrip("0123456789+-*/() ")
        if part.startswith('0'):
            return False
    return True

def apply_op(a, b, op):
    # Выполнение операции
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/':
        if b == 0:
            raise ZeroDivisionError("Ошибка: деление на ноль.")
        return a / b

def precedence(op):
    # Приоритет операций
    return 1 if op in "+-" else 2 if op in "*/" else 0

def evaluate_expression(expression):
    # Основная функция для вычисления выражения
    if not check_brackets(expression):
        return "Ошибка: скобки расставлены неверно."
    if not check_division_by_zero(expression):
        return "Ошибка: деление на ноль."

    expression = expression[:-1]  # Убираем "=" в конце
    values, ops = [], []
    i = 0

    while i < len(expression):
        if expression[i].isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = val * 10 + int(expression[i])
                i += 1
            values.append(val)
            i -= 1
        elif expression[i] == '(':
            ops.append(expression[i])
        elif expression[i] == ')':
            while ops and ops[-1] != '(':
                values.append(apply_op(values.pop(-2), values.pop(), ops.pop()))
            ops.pop()  # Убираем '('
        elif expression[i] in "+-*/":
            while ops and precedence(ops[-1]) >= precedence(expression[i]):
                values.append(apply_op(values.pop(-2), values.pop(), ops.pop()))
            ops.append(expression[i])
        i += 1

    while ops:
        values.append(apply_op(values.pop(-2), values.pop(), ops.pop()))

    return f"Результат: {values[0]}"

# Ввод выражения и вызов функции
expression = input("Введите математическое выражение: ")
if expression.endswith('='):
    print(evaluate_expression(expression))
else:
    print("Ошибка: выражение должно заканчиваться знаком '='.")
