"""Analyse a dictionary to find palingrams""" 

import load_dictionary
import time

word_list = load_dictionary.load('2of4brif.txt')

def min_word_length(words, min_length):
    """Filter list of words by minimum length"""
    filtered_words = []
    for word in words: 
        if len(word) > min_length: 
            filtered_words.append(word)
    print(filtered_words)
    return filtered_words


def find_palingrams():
    """Find dictionary palingrams.""" 
    pali_list = []
    word_list_filtered = min_word_length(word_list, 2)
    words = set(word_list_filtered)
    for word in words: 
        end = len(word)
        rev_word = word[::-1]
        if end > 1: 
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:])) 
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words: 
                    pali_list.append((rev_word[:end-i], word))
    return pali_list 

start_time = time.time()
palingrams = find_palingrams() 
end_time = time.time()

# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted: 
    print("{} {}".format(first, second))

print('Runtime was {} seconds.'.format(end_time - start_time))
 
