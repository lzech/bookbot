from stats import get_number_words
from stats import count_characters
from stats import sort_dict

def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()

def print_report(words_num, dic, path):
    tmp = []
    report = (("============ BOOKBOT ============\n"
              "Analyzing book found at ") + path + "\n"
              "----------- Word Count ----------\n"
              "Found " + str(words_num) + " total words\n"
              "--------- Character Count -------\n")
    for i in dic:
        if i[0].isalpha():
            report += str(i[0]) + ": " + str(i[1]) + "\n"
    return report
def main():
    path = "books/frankenstein.txt"
    number_words = get_number_words(get_book_text(path))
    sorted_dict = sort_dict(count_characters(get_book_text(path)))
    print(print_report(number_words, sorted_dict, path))
main()
