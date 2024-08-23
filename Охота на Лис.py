def create_field(size=8):
    # Создание пустого игрового поля
    field = [['.' for _ in range(size)] for _ in range(size)]
    return field

def display_field(field):
    size = len(field)
    # Отображение поля с нумерацией
    print("   " + "----" * size)  # Верхняя линия

    # Перебор строк в обратном порядке
    for index in range(size-1, -1, -1):
        print(f"{index + 1} |", end=" ")  # Нумерация строк 1-8
        print(" | ".join(field[index]) + " |")  # Объединим клетки с разделителем "|"
        print("   " + "----" * size)  # Линия между строками

    # Отображение английских букв снизу
    print("    " + "   ".join(chr(97 + i) for i in range(size)))  # Английские буквы a-h

def main():
    size = 8  # Размер поля 8x8
    field = create_field(size)
    display_field(field)

if __name__ == "__main__":
    main()