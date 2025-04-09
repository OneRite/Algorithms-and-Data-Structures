#10.	Задача о бросании яиц: Дано 100-этажное здание. Если яйцо 
# сбросить с высоты N-го этажа (или с большей высоты), оно разобьется. 
# Если его бросить с любого меньшего этажа, оно не разобьется. 
# У вас есть два яйца. Найдите N за минимальное количество бросков.


def egg_drop_2_eggs_100_floors():
    total_floors = 100
    # Найдём минимальное x, такое что x(x+1)/2 >= 100
    x = 1
    while (x * (x + 1)) // 2 < total_floors:
        x += 1

    # Список этажей, с которых мы будем бросать первое яйцо
    floors_to_try = []
    current = 0
    step = x
    while current < total_floors:
        current += step
        floors_to_try.append(min(current, total_floors))  # не выходим за пределы
        step -= 1

    print(f"Бросать 1-е яйцо по этажам: {floors_to_try}")
    print(f"Максимальное количество бросков в худшем случае: {x}")

    return x, floors_to_try

egg_drop_2_eggs_100_floors()
