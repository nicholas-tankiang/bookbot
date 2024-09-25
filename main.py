def main():
    path_to_file = "books/frankenstein.txt"
    
    text = get_book_path(path_to_file)
    print(text)

# return read of given path
def get_book_path(path):
    with open(path) as f:
        return f.read()

main()