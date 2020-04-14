"""Identify palindromes using a recursive algorithm."""
import load_dictionary

WORDLIST = load_dictionary.load('2of4brif.txt')

def find_palindromes_recursive():
    """Apply recursive first and last letter checking to determine if a word is a palindrome."""
    palindrome_list = []
    for word in WORDLIST:
        check = True
        test_word = word #word copy with first and last letter stripped recursively below
        while True:
            if len(test_word) <= 1:
                palindrome_list.append(word)
                break
            else:
                check = check_first_last(test_word)
                if check:
                    test_word = test_word[1:len(test_word)-1]
                    continue
                break
    return palindrome_list


def check_first_last(word):
    """Return boolean of whether the first and last letter in word are the same."""
    length = len(word)
    return word[0] == word[length - 1]


palindromes = find_palindromes_recursive()
print(*palindromes, sep='\n')
