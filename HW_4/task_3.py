"""✔ Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список."""
AMOUNT_MULTIPLE_OPERATIONS = 50
LIMIT_BALANCE = 5000000
COUNT_OPERATIONS = 3
MAX_SUM_WITHDRAW = 600
MIN_SUM_WITHDRAW = 30
WITHDRAWAL_PERCENTAGE = 0.015
INTEREST_ACCRUES = 1.03
WEALTH_TAX = 0.1

BALANCE = 0
TOTAL_WITHDRAWALS = 0
transactions = []


def deposit(amount):
    """Функция пополнения счёта"""
    global BALANCE, TOTAL_WITHDRAWALS
    if not amount % AMOUNT_MULTIPLE_OPERATIONS:
        BALANCE += amount
        TOTAL_WITHDRAWALS += 1
        transactions.append(('deposit', amount))
    else:
        print("Error!! Enter deposit amount (multiple of 50): ")

    if not TOTAL_WITHDRAWALS % COUNT_OPERATIONS:
        BALANCE *= INTEREST_ACCRUES

    if BALANCE > LIMIT_BALANCE:
        BALANCE -= BALANCE * WEALTH_TAX

    print("Your balance is now:", BALANCE)


def withdraw(amount):
    """Функция снятия денег"""
    global BALANCE, TOTAL_WITHDRAWALS
    if amount > BALANCE:
        print("Insufficient funds")
    elif amount % AMOUNT_MULTIPLE_OPERATIONS:
        print("Error!! Enter deposit amount (multiple of 50): ")
    else:
        BALANCE -= amount
        fee = max(MIN_SUM_WITHDRAW, min(amount * WITHDRAWAL_PERCENTAGE, MAX_SUM_WITHDRAW))
        BALANCE -= fee
        TOTAL_WITHDRAWALS += 1
        transactions.append(('withdraw', amount))

        if not TOTAL_WITHDRAWALS % COUNT_OPERATIONS:
            BALANCE *= INTEREST_ACCRUES

    if BALANCE > LIMIT_BALANCE:
        BALANCE -= BALANCE * WEALTH_TAX

    print("Your balance is now:", BALANCE)


def main():
    """Main"""
    while True:
        print("\nChoose an action: ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            amount = int(input("Enter deposit amount (multiple of 50): "))
            deposit(amount)

        elif choice == "2":
            amount = int(input("Enter withdrawal amount (multiple of 50): "))
            withdraw(amount)

        elif choice == "3":
            print("Thank you for using this ATM!")
            break

        else:
            print("Invalid input. Please enter a valid choice.")

    with open("transactions.txt", "w") as file:
        for transaction in transactions:
            file.write(f"{transaction[0]} {transaction[1]}\n")


main()
