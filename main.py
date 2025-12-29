from stats import get_number_words
from stats import count_characters

def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()


def main():
    print("Found", get_number_words(get_book_text('books/frankenstein.txt')), "total words")
    print(count_characters(get_book_text('books/frankenstein.txt')))

main()
