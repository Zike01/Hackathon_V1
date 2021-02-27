"""
4 - Write a function that simulates a guessing game. Player two should pick a number between 1
and 10. Player one then should guess the number. If they guess the right number they win. If they
guess the wrong number, Player two should say if their number is higher or lower. Player one
should guess again and keep guessing until they get the right number
"""


def game():
    number = int(input("Player two, pick a number between 1 and 10: "))

    if 1 <= number <= 10:

        should_continue = True
        while should_continue:
            choice = int(input("Player one, guess the number: "))
            if choice == number:
                print("You win!")
                should_continue = False
            elif choice < number:
                print("Too low, try again")
            elif choice > number:
                print("Too high, try again.")
    else:
        print("That is not a valid number, please try again.")
        game()


game()
