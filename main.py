from word_counter import *

def main():
    # directory of text
    path_to_file = "books/frankenstein.txt"
    print_report(path_to_file)

# return read of given path
def get_book_path(path):
    with open(path) as f:
        return f.read()

# convert dictionary of chars into a list of dictionary chars
def convert_dict(char_dict):
    list_chars = []
    for char in char_dict:
        current_dict = {}
        current_dict["char"] = char
        current_dict["count"] = char_dict[char]
        list_chars.append(current_dict)
    return list_chars

# Takes dictionary, return value of "count"
def sort_dict(list_chars):
    return list_chars["count"]

# sort result of convert_dict by "count", print formatted char count for each char
def print_dict(list_chars):
    converted_dict = convert_dict(list_chars)
    converted_dict.sort(reverse = True, key = sort_dict)
    for char in converted_dict:
        print(f"The '{char["char"]}' character was found {char["count"]} times.")

# prints formatted report 
def print_report(path_to_file):
    # line 1
    print(f"--- Report of {path_to_file}: Start ---")

    # line 2
    word_count = count_words(path_to_file)
    print(f"{word_count} words in text")

    # lines 3+
    char_dict = count_char(path_to_file)
    print_dict(char_dict)

    # line last
    print("--- End of report ---")

main()