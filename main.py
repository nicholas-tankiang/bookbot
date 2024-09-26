from word_counter import *

def main():
    path_to_file = "books/frankenstein.txt"

    # text = get_book_path(path_to_file)
    # print(text)

    word_count = count_words(path_to_file)
    print(f"{word_count} words in text")

    char_count = count_char(path_to_file)

# return read of given path
def get_book_path(path):
    with open(path) as f:
        return f.read()

main()