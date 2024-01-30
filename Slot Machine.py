import random

def deposit(balance):
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return balance + amount


def num_lines():
    while True:
        lines = input(f"How many lines do you want to bet on? 1-3 ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        amount = input(f"How much would you like to bet on each line? $1-$1000 ")
        if amount.isdigit():
            amount = int(amount)
            if 1 <= amount <= 1000:
                break
            else:
                print(f"Amount must be between $1 - $1000.")
        else:
            print("Please enter a number.")
    return amount


def get_slot_machine_spin():
    all_symbols = []
    symbol_count = {"S": 2, "A": 4, "B": 6, "C": 8}
    for symbol, symbol_count in symbol_count.items():
        all_symbols.extend([symbol] * symbol_count)
    columns = [[random.choice(all_symbols) for _ in range(3)] for _ in range(3)]
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()



def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)
    return winnings, winning_lines


def spin(balance):
    lines = num_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total Bet is equal to ${total_bet}")
    slots = get_slot_machine_spin()
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, {"S": 2, "A": 4, "B": 6, "C": 8})
    print(f"You won ${winnings}.")
    print(f"You won on", *winning_lines)
    return balance + winnings - total_bet


def main():
    balance = deposit(0)
    while True:
        print(f"Current balance is ${balance}")
        spn = input("Press enter to play (q to quit). ")
        if spn.lower() == "q" or spn.lower() == "quit":
            break
        balance = spin(balance)
    print(f"You left with ${balance}")



main()
