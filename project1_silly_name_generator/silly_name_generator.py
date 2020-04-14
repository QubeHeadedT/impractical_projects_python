# PROJECT1: Silly Name generator

import sys, random


def main():

    print("Welcome to the Psych 'Sidekick Name Picker.' \n")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ('Baby Oil', 'Bad News', 'Big Burps', 'Stickbug', 'Mantis', 'Ladybird')

    last = ('Kansas', 'Arkansas', 'Tickle', 'Johnson', 'Sackrider', 'Winterkorn')
    while True:
        firstName = random.choice(first)

        lastName = random.choice(last)

        print("\n\n")
        print("{} {}".format(firstName, lastName), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

if __name__ == "__main__":
    main()
    