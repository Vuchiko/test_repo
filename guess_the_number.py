import random
import sys
import time
import os


class GTNRunner:

    def __init__(self):
        self.welcome_banner()
        self.level = self.select_level()
        self.__secret_number = random.randint(1, self.level)
        self.result = self.run_the_game()
        if self.result == 'success':
            self.goodbye_banner()

    def goodbye_banner(self):
        pass

    def welcome_banner(self):
        pass

    def select_level(self):
        input_value = input("Are you:\n1) Chancellor\n2) Jedi\n3) Padawan"
                            "\nSelect the level: ")
        if input_value.lower() in ["chancellor", '1']:
            self.terminal_cleaner()
            print('You are Chancellor and have '
                  '100 possible numbers in front of you.')
            return 100
        elif input_value.lower() in ['jedi', '2']:
            self.terminal_cleaner()
            print('You are Jedi and have '
                  '50 possible numbers in front of you.')
            return 50
        elif input_value.lower() in ['padawan', '3']:
            self.terminal_cleaner()
            print('You are Padawan and have '
                  '10 possible numbers in front of you.')
            return 10
        else:
            self.terminal_cleaner()
            print('Sorry, but you have to be one of a kind.')
            sys.exit(1)

    @staticmethod
    def terminal_cleaner():
        pass

    def validate_input(self, value):
        try:
            float(value)
        except ValueError:
            print('You seek for a number, not for a holy grall.')
            sys.exit(1)
        try:
            int(value)
        except ValueError:
            print('\nNo,no. . . decimal numbers are not allowed.'
                  '\nReturning 404.')
            time.sleep(2)
            self.terminal_cleaner()
            return 404
        return value

    def run_the_game(self):
        number_found = False
        number_of_tries = 1

        while not number_found:
            your_guess = int(self.validate_input(input('Make a guess: ')))
            self.terminal_cleaner()
            if self.__secret_number == your_guess:
                self.terminal_cleaner()
                print(
                    f'You have successfully found magic '
                    f'number {self.__secret_number} !!!')
                if number_of_tries < 2:
                    print(f'Fast and furious !!! . . . '
                          f'Got it from very first attempt.')
                else:
                    print(f'Nice. You spent {number_of_tries} '
                          f'guesses for finding it.')
                return 'success'
            else:
                number_of_tries += 1
                print("Hm, you missed this time. Let's try again!")
                if your_guess > self.__secret_number:
                    print(
                        f'Hint :-) . . . your guess {"-" * number_of_tries} '
                        f'{your_guess} {"-" * number_of_tries} was too high.')
                else:
                    print(
                        f'Hint :-) . . . your guess {"-" * number_of_tries} '
                        f'{your_guess} {"-" * number_of_tries} was too low.')
                continue


class GTNRunner_Windows(GTNRunner):

    def __init__(self):
        super().__init__()

    def goodbye_banner(self):
        print('#' * 120)
        print('\t' * 5 + ' ' * 4 + '. . .Goodbye . . .' + ' ' * 4 + '\t' * 5)
        print('#' * 120)

    def welcome_banner(self):
        print('#' * 120)
        print('\t' * 5 + ' ' * 4 + 'Welcome to the game' + ' ' * 4 + '\t' * 5)
        print('#' * 120)

    @staticmethod
    def terminal_cleaner():
        os.system('cls')


class GTNRunner_Linux_MacOS(GTNRunner):
    try:
        import pyfiglet
    except ImportError:
        print('Please install pyfiglet module.')
        print('\nTrying to install pyfiglet. . . \n')
        os.system('pip3 install pyfiglet')
        import pyfiglet
        print('\nStarting the game . . .\n\n')

    def __init__(self):
        super().__init__()

    def goodbye_banner(self):
        self.pyfiglet.print_figlet("Congrats !",
                                   font='starwars',
                                   colors="0;255;0", width=200)

    def welcome_banner(self):
        self.pyfiglet.print_figlet("Guess  the  Number\n",
                                   font='starwars',
                                   colors="0;255;0", width=200)

    @staticmethod
    def terminal_cleaner():
        os.system('clear')


if __name__ == '__main__':
    try:
        if os.name == 'nt':
            number = GTNRunner_Windows()
        else:
            number = GTNRunner_Linux_MacOS()
    except KeyboardInterrupt:
        print("\nGoodbye. . . Thank you for your play.")
        sys.exit(1)
