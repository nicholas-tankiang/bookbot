# can change to accept user input of path
# for now, hardcoded to books/frankenstein.txt
# return a string, given path to text
path = "books/frankenstein.txt"
def get_text(path):
    with open(path) as f:
        return f.read()

# split string of text given path
def split_text(path):
    text_list = get_text(path).split()
    # for testing:
    # print(text_list[:10])
    return text_list

# return word count given path
def count_words(path):
    word_count = 0
    for word in split_text(path):
        word_count += 1
        # for testing:
        # print(word_count)
    return word_count