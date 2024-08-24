import random


def create_field(size=8):
    # Создание пустого игрового поля
    field = [['.' for _ in range(size)] for _ in range(size)]
    return field


def place_foxes(field, num_foxes=8):
    size = len(field)
    placed_positions = set()  # Множество для отслеживания размещенных позиций

    while len(placed_positions) < num_foxes:
        # Генерируем случайные координаты для размещения лисы
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)

        # Проверяем, не занята ли позиция
        if (row, col) not in placed_positions:
            field[row][col] = '\033[31m\033[1mL\033[0m'  # Размещаем лису красным жирным цветом
            placed_positions.add((row, col))  # Запоминаем размещенную позицию


def display_field(field):
    size = len(field)
    # Отображение поля с нумерацией
    print("   " + "----" * size)  # Верхняя линия

    # Перебор строк в обратном порядке
    for index in range(size - 1, -1, -1):
        print(f"{index + 1} |", end=" ")  # Нумерация строк 1-8
        print(" | ".join(field[index]) + " |")  # Объединим клетки с разделителем "|"
        print("   " + "----" * size)  # Линия между строками

    # Отображение английских букв снизу
    print("    " + "   ".join(chr(97 + i) for i in range(size)))  # Английские буквы a-h


def count_foxes_in_line(field, row, col):
    size = len(field)
    count = 0

    # Проверяем горизонталь
    for c in range(size):
        if field[row][c] == '\033[31m\033[1mL\033[0m':
            count += 1

    # Проверяем вертикаль
    for r in range(size):
        if field[r][col] == '\033[31m\033[1mL\033[0m':
            count += 1

    # Вычитаем 1, так как текущая позиция учитывается в обоих подсчетах
    if field[row][col] == '\033[31m\033[1mL\033[0m':
        count -= 1

    return count


def shoot(field, position):
    size = len(field)
    # Преобразуем введённую координату
    if len(position) == 2 and position[0] in 'abcdefgh' and position[1] in '12345678':
        col = ord(position[0]) - ord('a')  # Преобразуем букву столбца в индекс
        row = int(position[1]) - 1  # Преобразуем цифру строки в индекс

        # Проверяем, находится ли координата в пределах поля
        if 0 <= row < size and 0 <= col < size:
            if field[row][col] == '\033[31m\033[1mL\033[0m':  # Если там лиса
                print("\033[32m\033[1mПопадание! Вы убили лису!\033[0m")  # Зеленый жирный текст
                field[row][col] = '.'  # Удаляем лису с поля
                # Обновляем количество лис в клетке
                fox_count = count_foxes_in_line(field, row, col)
                field[row][col] = str(fox_count)  # Записываем количество лис в клетку
                return True, fox_count  # Возвращаем True и количество лис
            else:
                # Подсчет лис по вертикалям и горизонталям
                fox_count = count_foxes_in_line(field, row, col)
                field[row][col] = str(fox_count)  # Записываем количество лис в клетку
                print("\033[31m\033[1mПромах!\033[0m")  # Красный жирный текст
                return False, fox_count  # Возвращаем False и количество лис
        else:
            print("Выход за пределы поля!")
            return False, 0
    else:
        print("Неверный ввод, попробуйте снова.")
        return False, 0


def main():
    size = 8  # Размер поля 8x8
    field = create_field(size)
    place_foxes(field)  # Размещаем 8 лис на поле
    display_field(field)

    moves_count = 0  # Счетчик ходов

    while True:
        print()  # Добавляем пустую строку для отступа
        command = input("Введите координаты для выстрела (например, a1) или 'q' для выхода: ")
        if command == 'q':
            break

        moves_count += 1  # Увеличиваем счетчик ходов
        hit, fox_count = shoot(field, command)  # Обрабатываем выстрел
        display_field(field)  # Отображаем поле после выстрела

        # Проверяем, остались ли лисы на поле
        if all(cell != '\033[31m\033[1mL\033[0m' for row in field for cell in row):
            print()  # Добавляем пустую строку для отступа перед сообщением
            print(f"ПОЗДРАВЛЯЕМ, ВЫ РАССПРАВИЛИСЬ С ЛИСАМИ ЗА: {moves_count} ХОДОВ!")
            break  # Завершаем игру, если лисы убиты
        else:
            print(f"Количество лис по вертикалям и горизонталям: {fox_count}")  # Вывод количества лис


if __name__ == "__main__":
    main()
