import random

MAX_LINES = 3 # easily changable 
MAX_BET = 100
MIN_BET = 1 # constants

ROWS = 3
COLS = 3

#dict of the count of symbols
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

# value of each symbol
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings= 0 #initial winnings
    winning_lines = []
    for line in range(lines): #works dynamiclly/ every line in the lines
        symbol = columns[0][line] #first column because first symbol then check which line
        for column in columns: # loops through every column
            symbol_to_check = column[line] #symbol checks at the row we are at
            if symbol != symbol_to_check:
                break # break if not the same
        else: #runs if no break
            winnings += values[symbol] * bet # they won the bet of symbol of each line
            winning_lines.append(line + 1) # change from index into number of line 

    return winnings, winning_lines        






#generate the symbols
def get_slot_machine_spin(rows, cols, symbols): #parameters of the function
    all_symbols = [] #list
    for symbol, symbol_count in symbols.items(): #key and value
        for _ in range(symbol_count): #_ because we do not care about the count
            all_symbols.append(symbol) #added symbol twice into the list

    columns = [] # def column list
    for _ in range(cols): # for every column
        column = [] # column is equal to an empty list
        current_symbols = all_symbols[:] #copy of the list and select from copy
        for _ in range(rows): 
            value = random.choice(current_symbols) #remove symbol from current list
            current_symbols.remove(value)
            column.append(value) #adds value 

        columns.append(column)  # add column to column list
        
    return columns

#transposing
def print_slot_machine(columns):
    for row in range(len(columns[0])): #assumes we at least have one column
        for i, column in enumerate(columns): # looping through all the iteams in the column list/ gives you index as well as iteam
            if i !=len(columns) - 1: #max index in the column list
                print(column[row], end="|") #pipe operator/ separte iteams
            else:
                print(column[row], end="") #row inside the column/ if max length dont print pipe

        print()  # next line          





#collecting user input
def deposit(): #collecting user input collecting user deposit
    #function is something we can call thats going to execute line of code and return a value
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): #checks if the number is digits
            amount = int(amount) #first check if they entered a digit
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else: 
            print("Please enter a number.")

    return amount  

#collect bet from user/get number of lines from user
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+ str(MAX_LINES) + ")? ") # str converts max lines as a part of the sentence
        if lines.isdigit(): #checks if the number is digits
            lines = int(lines) #first check if they entered a digit
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else: 
            print("Please enter a number.")

    return lines  

#check amount to bet on each line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): #checks if the number is digits
            amount = int(amount) #first check if they entered a digit
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.") # auto convert to strings
        else: 
            print("Please enter a number.")

    return amount  




def spin(balance): # one single spin/ checks balance
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break    

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet} ")

    #generate the slot machine
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines) #splat operator
    return winnings - total_bet # how much they won or lost


def main(): #rerun program
    balance = deposit()  #calling for function
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance) # updates balance as a result of spin

    print(f"You left with ${balance}")    



    
    

main()    



