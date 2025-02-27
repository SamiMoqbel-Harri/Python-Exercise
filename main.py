# A random number between 1 - 100 will be generated and the user will try to guess that number.
# Whenever the user enters a wrong value the machine should hint him if the entered value is lower or greater
# than the generated one until he correctly guess it.
#
# Please write it in two forms:
# procedural way
# class based way
import random

def get_user_input():
    while True:
        try:
            return int(input('Guess a number between 1 and 100:\n'))
        except ValueError:
            print('Enter only Integers, please')

def procedural_game():
    target = random.randint(1, 100)
    user_input = get_user_input()
    while user_input != target:
        if user_input > target:
            print('Target is smaller than input, Try smaller value')
        else:
            print('Target is bigger than input, Try bigger value')

        user_input = get_user_input()

    print(f'Yay!!!, Congrats the number was : {target}')


class GuessingGame:
    _user_input = None

    def __init__(self):
        self._target = random.randint(1, 100)

    def get_input(self):
        while True:
            try:
                self._user_input = int(input('Guess a number between 1 and 100:\n'))
                return
            except ValueError:
                print('Enter only Integers, please')

    def show_win_message(self):
        print(f'CONGRATS You WON!!!, The target was {self._target}')

    def play_game(self):
        self.get_input()
        while self._user_input != self._target:
            if self._user_input > self._target:
                print('Target is smaller than input, Try smaller value')
            else:
                print('Target is bigger than input, Try bigger value')
            self.get_input()

        self.show_win_message()

if __name__ == "__main__":
    # procedural_game()
    game = GuessingGame()
    game.play_game()
