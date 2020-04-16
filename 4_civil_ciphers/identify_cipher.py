"""Analyses a ciphertext and predicts whether ciphtext is a transpostion or substitution cipher

Applies letter frequency analysis to predict cipher type. 
Compares ciphertext letter frequency against letter frequency proportion from military messages.
Letter frequency is unchanged for a letter transposition cipher (positions moved).
Letter frequency *IS* changed for a letter substitution cipher. 

Inputs: Ciphertext text filename, Military letter frequency text file, Threshold letter freqency difference

---Letter frequency table format---
Letter frequency given as a ratio of total letters.
Letters labelled in line 
26 lines - each new line indicating a letter.
(eg. 
A 0.0813
B 0.0345
etc) 
-----------------------------------

Outputs: Prints letter frequency comparison results and prediction of cipher type. 
"""
import sys
from collections import defaultdict
#==================================================================================================
# USER INPUT:

# The Ciphertext filename to be analysed: 
ciphertext_filename = 'cipher_b        .txt'

# Letter frequency table filename to compare against: 
military_frequency_filename = 'letter_frequency_military.txt'

# Threshold for classifying ciphers - substitution cipher if freq_diff > THRESHOLD
THRESHOLD = 1

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#==================================================================================================

def main():
    """Run the program and print a prediction"""
    # Load given files
    ciphertext = load_text(ciphertext_filename)
    military_frequency = load_letter_freq(military_frequency_filename)
    
    # Compare ciphertext letter frequency to given letter frequency
    ciphertext_freq = generate_freq(ciphertext) 
    freq_diff = compare_freq(ciphertext_freq, military_frequency)

    # Output results:
    print('\nThe difference in letter frequency totals: {}'.format(freq_diff))
    print('\nFrequency difference threshold = {}'.format(THRESHOLD))
    if (freq_diff - THRESHOLD) > 0:
        print('\n\nTherefore this is a letter substitution cipher.')
    else: 
        print('\n\nTherefore this is a letter transposition cipher.')
    

def load_text(filename): 
    """Load the given text file name to a string"""
    try: 
        with open(filename) as file:
            text = file.read().lower() # all text processed in lowercase
    except IOError as e: 
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)
    return text
    

def load_letter_freq(filename): 
    """Load the given letter frequency table and return as a dictionary"""
    letter_freq = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, \
        'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, \
            'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, \
                'y': 0, 'z': 0} # output dictionary
    freq_text = load_text(filename)
    letter_freq_line = freq_text.split('\n')

    # Generate dictionary values and keys
    for line in letter_freq_line:
        if line == '': 
            break
        (letter, freq) = line.split()
        letter_freq[letter] = float(freq)

    return letter_freq


def generate_freq(input_string):
    """Generates list of letter frequency as a proportion for 'text_in'"""
    stripped_string = ''.join(l for l in input_string if l.isalnum()) # only alphanumeric characters
    letter_freq = proportion_letters(stripped_string)
    
    return letter_freq


def proportion_letters(letter_list):
    """Generate proportion of letters in a lowercase alphanum letter list as a decimal. Output as dictionary."""
    proportion_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, \
        'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, \
            'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, \
                'y': 0, 'z': 0}
    list_len = len(letter_list)
    counter = defaultdict(int)

    for l in letter_list:
        counter[l] += 1

    # normalise by list length
    for letter, value in counter.items(): 
        value = value/list_len
        proportion_dict[letter] = value

    return proportion_dict


def compare_freq(freq1, freq2): 
    """Outputs the sum of differences between to letter frequency lists"""
    result = 0

    # sum differences across letters
    for key, value in freq1.items():
        diff = abs(value - freq2[key])
        result += diff

    return result
    

if __name__ == '__main__':
    main() 


