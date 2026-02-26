from random import randint
# Your task: Write a Python script that:

# uses at least one variable
# includes a conditional
# includes a loop
# defines one function
# handles one possible error with try/except
# prints a useful or fun result
def baby_boo(win):
    if win:
        print("She gon call me baby boo")
    else:
        print("Womp womp")

def main():
    print("A secret message will be revealed " +
          "if you guess my secret number!")
    print("You have 5 tries.")
    secret_number = randint(1, 3)
    turns = 0
    win = False
    while turns < 5:
        guess = input(f"Guess a number from 1-3 (Try {turns + 1}/5): ")

        try:
            guess_int = int(guess)
            if guess_int < 1 or guess_int > 3:
                print("Error: Please enter a number between 1 and 3.")
                continue
            win = guess_int == secret_number
        except ValueError:
            print("Error: Not a number.")
            continue

        if win:
            break

        print(f"Lock in! {4 - turns} tries left.")
        turns += 1

    if not win:
        print(f"You ran out of tries! The number was {secret_number}.")

    print()
    baby_boo(win)
    print("See you later :)")

if __name__ == "__main__":
    main()