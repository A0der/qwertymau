def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y

def main():
    print("--- Простой калькулятор ---")
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: нужно вводить только числа!")
        return

    print("\nВыберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    
    choice = input("Ваш выбор (1/2/3/4): ")

    if choice == '1':
        print(f"Результат: {add(a, b)}")
    elif choice == '2':
        print(f"Результат: {subtract(a, b)}")
    elif choice == '3':
        print(f"Результат: {multiply(a, b)}")
    elif choice == '4':
        print(f"Результат: {divide(a, b)}")
    else:
        print("Неверный ввод!")

if __name__ == "__main__":
    main()