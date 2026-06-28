
history_file = "history.txt"

def save_history(text):
    with open(history_file, "a", encoding="utf-8") as file:
        file.write(text + "\n")

def show_history():
    try:
        with open(history_file, "r", encoding="utf-8") as file:
            print("\n История операций:")
            print(file.read())
    except FileNotFoundError:
        print("История пока пуста.")

while True:
    
    print("\n \t Калькулятор \n")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. История")
    print("0. Выход")

    choice = input("\n Выбери действие: ")

    if choice == "0":
        print("Пока, пока!")
        break

    elif choice == "5":
        show_history()

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
                if b == 0:
                    print("Ошибка: деление на ноль!")
                    continue

                result = a / b
                operation = f"{a} / {b} = {result}"

            print("Результат:", result)

            save_history(operation)

        except ValueError:
            print("Ошибка: нужно вводить числа!")

    else:
        print("Неверный пункт меню!")