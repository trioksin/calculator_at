# Имя файла, в котором будет храниться история вычислений
history_file = "history.txt"

"""
Функция сохранения истории вычислений.
Данная функция была реализована с использованием ChatGPT.
Она открывает файл history.txt в режиме добавления ("a")
и записывает в него новую выполненную операцию
"""
def save_history(text):
    with open(history_file, "a", encoding="utf-8") as file:
        file.write(text + "\n")

"""
Функция отображения истории вычислений.
Данная функция также была реализована с использованием ChatGPT.
Она открывает файл history.txt, считывает его содержимое
и выводит историю на экран.
Если файл отсутствует, выводится соответствующее сообщение
"""
def show_history():
    try:
        with open(history_file, "r", encoding="utf-8") as file:
            print("\n История операций:")
            print(file.read())
    except FileNotFoundError:
        print("История пока пуста.")

# Основной цикл. Работает до тех пор, пока пользователь не выберет пункт "Выход"

while True:
    
    print("\n \t Калькулятор \n")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. История")
    print("0. Выход")

 # Запрос выбора действия
    choice = input("\n Выбери действие: ")

    # Завершение работы
    if choice == "0":
        print("Пока, пока!")
        break

# Просмотр истории вычислений
    elif choice == "5":
        show_history()
    # Выполнение арифметических операций
    elif choice in ["1", "2", "3", "4"]:

        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))

            if choice == "1":
                result = a + b
                operation = f"{a} + {b} = {result}"

            elif choice == "2":
                result = a - b
                operation = f"{a} - {b} = {result}"

            elif choice == "3":
                result = a * b
                operation = f"{a} * {b} = {result}"

            elif choice == "4":
                if b == 0: # Проверка деления на ноль
                    print("Ошибка: деление на ноль!")
                    continue

                result = a / b
                operation = f"{a} / {b} = {result}"

            print("Результат:", result)

            save_history(operation) # Сохранение операции в файл истории
        except ValueError: # Обработка ошибки,если пользователь ввёл не число
            print("Ошибка: нужно вводить числа!")

    else: # Если выбран неизвестный пункт меню
        print("Неверный пункт меню!")