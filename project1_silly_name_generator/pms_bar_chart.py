"""Poor man's bar chart challenge from project 1"""

from collections import defaultdict
import pprint

def get_input():
    """Requests text input, decapitalises, removes spaces and
    non-alphabetical characters and returns"""
    input_string = input("\nInput a sentence to convert!\n").lower()
    stripped_string = ''.join(l for l in input_string if l.isalnum())

    return stripped_string

def count_letters(input_string):
    """Takes string (without spaces or capitals) as input,
    returns a dictionary counting the number of times each
    letter appears in the string"""
    count_dict = defaultdict(int)

    for l in input_string:
        count_dict[l] += 1

    return count_dict

def print_dict(dict):
    """Takes a dictionary of letter count as input and prints
    in a 'poor man's bar chart' format"""
    pp = pprint.PrettyPrinter(sort_dicts=True)
    pp.pprint(dict)

    return


if __name__ == "__main__":
    text = get_input()
    letter_count = count_letters(text)
    print_dict(letter_count)
