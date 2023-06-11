from decimal import Decimal, ROUND_DOWN

# Класс "Банкомат".
class ATM:

    TRIGGER_SUM = Decimal(5000000).quantize(Decimal('0.00'), rounding=ROUND_DOWN)

    operation_count: int
    balance: Decimal
    wealth_tax: Decimal
    add_percentage: Decimal

    def __init__(self, operation_count: int, balance: Decimal, wealth_tax: Decimal, add_percentage: Decimal) -> None:
        self.operation_count = operation_count
        self.balance = balance
        self.wealth_tax = wealth_tax
        self.add_percentage = add_percentage

    # Метод, возвращающий номер выбранного пользователем действия Банкомата.
    def chosen_option(self) -> int:
        user_choice = input("Выберите номер действия: ")

        while not user_choice.isdigit() or int(user_choice) > 3:
            user_choice = input("Ошибка! Выберите номер действия: ")

        return int(user_choice)

    # Метод для продолжения работы с банкоматом после успешной итерации.
    def continue_operations(self) -> bool:
        print()
        user_choice = input("Продолжить работу? (y / n): ")

        while not ((user_choice == 'y') or (user_choice == 'n')):
            user_choice = input(
                "Вы ввели недопустимое значение! Продолжить работу? (y / n): ")

        if user_choice == 'y':
            return True

        else:
            return False
    
    # Метод для пополнения счета.
    def replenish(self) -> None:
        print()
        print(f"Ваш текущий баланс: {self.balance}")
        self.wealth_tax = Decimal(self.wealth_tax).quantize(Decimal('0.00'), rounding=ROUND_DOWN)
        tax_value = 0

        if self.balance > self.TRIGGER_SUM:
            tax_value = (self.balance * self.wealth_tax).quantize(Decimal('0.00'), rounding=ROUND_DOWN)
            print(f"Налог на богатство ({self.wealth_tax}%): {tax_value}!")
            self.balance -= tax_value
            print(f"Ваш текущий баланс: {self.balance}")
            print()

        amount = input("Введите желаемую сумму пополнения: ")

        while not (amount.isdigit()) or not (int(amount) % 50 == 0):
            print("Вы ввели недопустимое значение!")
            amount = input(
                "Введите при помощи цифр желаемую сумму пополнения, кратную 50: ")

        self.balance = Decimal(self.balance) + Decimal(amount)
        self.operation_count += 1

        if self.operation_count % 3 == 0:
            self.balance = (Decimal(self.balance) + Decimal(self.balance)
                            * Decimal(self.add_percentage)).quantize(Decimal('0.00'), rounding=ROUND_DOWN)

        print(f"Баланс пополнен успешно! Текущее значение баланса: {self.balance}")

    # Метод для снятия средств.
    def withdraw(self) -> None:
        print()
        print(f"Ваш текущий баланс: {self.balance}")
        self.wealth_tax = Decimal(self.wealth_tax).quantize(Decimal('0.00'), rounding=ROUND_DOWN)
        tax_value = 0

        if self.balance > self.TRIGGER_SUM:
            tax_value = (self.balance * self.wealth_tax
                         ).quantize(Decimal('0.00'), rounding=ROUND_DOWN)
            print(f"Налог на богатство ({self.wealth_tax}%): {tax_value}!")
            self.balance -= tax_value
            print(f"Ваш текущий баланс: {self.balance}")
            print()

        added_value = 0
        amount = input("Введите желаемую сумму снятия: ")

        while not (amount.isdigit()):
            print("Вы ввели недопустимое значение!")
            amount = input(f"Введите при помощи цифр желаемую сумму снятия: ")

        additional_withdraw = Decimal(amount) * Decimal(0.015)

        if 30 >= additional_withdraw:
            additional_withdraw = 30

        if additional_withdraw >= 600:
            additional_withdraw = 600

        amount = Decimal(amount) + additional_withdraw

        if amount > self.balance:
            print(f"Невозможно снять {amount} у.е. (с учетом процента за снятие), т.к. Ваш баланс = {self.balance} у.е.")

        else:
            self.balance = Decimal(self.balance) - amount
            self.operation_count += 1

            if self.operation_count % 3 == 0:
                added_value = (Decimal(self.balance) * Decimal(self.add_percentage)
                               ).quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                self.balance = (Decimal(
                    self.balance) + added_value).quantize(Decimal('0.00'), rounding=ROUND_DOWN)

            print(f"Комиссия за операцию снятия: ({additional_withdraw}).")
            print(f"Т.к. порядковый номер операции - {self.operation_count}, к балансу добавлено {added_value}!")
            print(f"Ваш текущий баланс: {self.balance}")
