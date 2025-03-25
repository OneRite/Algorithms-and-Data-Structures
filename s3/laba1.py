def checking (string):
    stack = [] #LIFO
    matching = {'(': ')', '{': '}', '[': ']'}
    
    for char in string: 
        if char in matching:
            stack.append(char)
        elif char in matching.values():
            if not stack or matching[stack.pop()] != char: #проверка совпадет ли 
                #текущая закрывающая скобка и соответствующая ей открывающая скобка
                return "Строка не существует"
    
    if not stack:
        return "Строка существует"
    else:
        return "Строка не существует"

string = input("Введите строку: ")
print(checking(string))
