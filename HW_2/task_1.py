# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю.
# ✔ Допустимые действия: пополнить, снять, выйти.
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%.
# ✔ Нельзя снять больше, чем на счёте.
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной.
# ✔ Любое действие выводит сумму денег.

BALANCE = 0
TOTAL_WITHDRAWALS = 0
MULTIPLE = 50
MAX_BALANCE = 5_000_000
RATE = 0.1
COUNT = 3
MIN_MANY = 30
MAX_MANY = 600
PERCENT_1 = 0.015
PERCENT_2 = 1.03

while True:
    print("\nChoose an action: ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        amount = int(input("Enter deposit amount (multiple of 50): "))
        if amount % MULTIPLE == 0:
            BALANCE += amount
            TOTAL_WITHDRAWALS += 1
        else:
            print("Error!! Enter deposit amount (multiple of 50): ")
        if TOTAL_WITHDRAWALS % COUNT == 0:
            BALANCE *= PERCENT_2
        if BALANCE > MAX_BALANCE:
            BALANCE = BALANCE - (BALANCE * RATE)
        print("Your balance is now:", BALANCE)

    elif choice == "2":
        amount = int(input("Enter withdrawal amount (multiple of 50): "))
        if amount > BALANCE:
            print("Insufficient funds")
        elif amount % MULTIPLE != 0:
            print("Error!! Enter deposit amount (multiple of 50): ")
        else:
            BALANCE -= amount
            fee = max(MIN_MANY, min(amount * PERCENT_1, MAX_MANY))
            BALANCE -= fee
            TOTAL_WITHDRAWALS += 1
            if TOTAL_WITHDRAWALS % COUNT == 0:
                BALANCE *= PERCENT_2
        if BALANCE > MAX_BALANCE:
            BALANCE = BALANCE - (BALANCE * RATE)
        print("Your balance is now:", BALANCE)

    elif choice == "3":
        print("Thank you for using this ATM!")
        break

    else:
        print("Invalid input. Please enter a valid choice.")
