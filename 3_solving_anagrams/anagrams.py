import load_dictionary
import sys

WORDLIST = load_dictionary.load('2of4brif.txt')

anagram_list = [] 

def check_input(word):
    """ Check the input is not a null string and contains no spaces. """
    if len(word) < 1:
        print("Error, no word entered. Exiting program. ", file = sys.stderr)
        sys.exit(1)

    stripped_word = word.replace(' ', '')

    if len(name) != len(stripped_word): 
        print("Error, please only enter one word.", file = sys.stderr)
        sys.exit(1) 

# input a single word or single name below to find its anagram(s):
name = input("\nWhat anagram would you like to solve?\n")

check_input(name)

print("Input name = {}".format(name))
name = name.lower()
print("Using name = {}".format(name))

# sort name and find anagrams
name_sorted = sorted(name)
for word in WORDLIST: 
    word = word.lower()
    if word != name: 
        if sorted(word) == name_sorted:
            anagram_list.append(word)

# print out a list of anagrams
print()
if len(anagram_list) == 0:
    print("No anagrams found.")
else: 
    print("Anagrams =", *anagram_list, sep='\n') 