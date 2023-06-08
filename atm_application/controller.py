import view
from model import ATM

# Константы, нужные для работы методов класса "Банкомат"
DEFAULT_OPERATIONS = 0
DEFAULT_BALANCE = 0
WEALTH_TAX = 0.1
ADD_PERCENTAGE = 0.03


def button():
    session = ATM(operation_count=DEFAULT_OPERATIONS, balance=DEFAULT_BALANCE,
                  wealth_tax=WEALTH_TAX, add_percentage=ADD_PERCENTAGE)
    view.menu()
    user_choice = session.chosen_option()

    while user_choice == 1:
        session.replenish()
        if session.continue_operations():
            view.menu()
            user_choice = session.chosen_option()
            continue
        else:
            view.goodbye()
            break

    while user_choice == 2:
        session.withdraw()
        if session.continue_operations():
            view.menu()
            user_choice = session.chosen_option()
            continue
        else:
            view.goodbye()
            break

    if user_choice == 3:
        view.goodbye()
