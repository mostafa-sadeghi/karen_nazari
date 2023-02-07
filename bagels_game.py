import random
NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(f'''Welcome to our bagels game!
    we are going to guess {NUM_DIGITS} digits number, and we have {MAX_GUESSES} times to guess!
    When i Say :            That means:
    Pico                        one digit is correct but not in the right position!
    Fermi                       one digit is correct and in the right position!
    Bagels                      No Digit is correct!
    ''')

    while True:
        # todo our game's core codes
        # generate 3 digits secretnumber
        # ask the user to enter the guess
        # check user's guess and send him a hint


if __name__ == '__main__':
    main()
