"""Generate some funny names based on two lists and print to screen."""

import sys
import random


def main():
    """Choose names from two tuples at random and print them onto the screen as one name."""
    print("Welcome to the Psych 'Sidekick Name Picker.' \n")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ('Baby Oil', 'Bad News', 'Big Burps', 'Stickbug',
    	'Mantis', 'Ladybird')

    last = ('Kansas', 'Arkansas', 'Tickle', 'Johnson',
    	'Sackrider', 'Winterkorn')

    middle = ('"Kiddy Fiddler"', '"The Tickler"', '"Toothbrush"', '"Midnight Brown"')

    while True:
        first_name = random.choice(first)

        if random.randint(1, 3) == 3:
            middle_name = random.choice(middle)
        else:
            middle_name = ''

        last_name = random.choice(last)

        print("\n")
        if middle_name == '':
            print("{} {}".format(first_name, last_name))
        else:
            print("{} {} {}".format(first_name, middle_name, last_name), file=sys.stderr)
        print("\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

if __name__ == "__main__":
    main()
