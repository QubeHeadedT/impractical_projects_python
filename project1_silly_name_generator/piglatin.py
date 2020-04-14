"""A function which takes a test input, converts it to pig latinand prints the result to the screen."""
def main():
    """
    Run pig latin converter.

    A function which takes a test input, converts it to pig latin
    and prints the result to the screen.
    """
    text = input("\n\nInput a sentence to convert!\n").lower()
    words = text.split()
    converted_words = []
    output_string = ""

    for word in words:
        converted_words.append(convert_word(word))

    for word in converted_words:
        output_string = output_string + word + ' '

    output_string = output_string.strip() + '.'
    print(output_string.capitalize())


def convert_word(word):
    """Take individual word as input and return word converted to pig latin in lower case."""
    word_length = len(word)
    pig_word = word[1:word_length-1] + word[0] + 'ay'
    return pig_word


if __name__ == "__main__":
    main()
