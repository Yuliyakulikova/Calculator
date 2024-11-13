class Operation:
    def execute(self, num1, num2):
        raise NotImplementedError("Must override execute")


class Addition(Operation):
    def execute(self, num1, num2):
        return num1 + num2


class Subtraction(Operation):
    def execute(self, num1, num2):
        return num1 - num2


class Multiplication(Operation):
    def execute(self, num1, num2):
        return num1 * num2


class Division(Operation):
    def execute(self, num1, num2):
        if num2 == 0:
            raise ValueError("Error: Division by zero is not allowed!")
        return num1 / num2


class Calculator:
    def __init__(self):
        self.operations = {
            '1': Addition(), # Сложение
            '2': Subtraction(), # Вычитание
            '3': Multiplication(), # Умножение
            '4': Division(), # Деление
        }

    def calculate(self, operation_code, num1, num2):
        if operation_code in self.operations:
            return self.operations[operation_code].execute(num1, num2)
        else:
            raise ValueError("Unknown operation")

    def run(self):
        while True:
            num1 = int(input("Введите первое число: "))
            num2 = int(input("Введите второе число: "))
            print("Выберите операцию:\n1. Сложение +\n2. Вычитание -\n3. Умножение *\n4. Деление /")
            operation_code = input()

            try:
                result = self.calculate(operation_code, num1, num2)
                print("Результат:", result)
            except ValueError as e:
                print(e)

            if input("Хотите продолжить? (1. Да, 2. Нет) \n") == '2':
                print("Спасибо за использование калькулятора!")
                break


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
