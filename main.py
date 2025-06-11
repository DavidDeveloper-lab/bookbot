from stats import *
import sys

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


relative_path = sys.argv[1]


def get_book_text(filepath):
    with open(filepath) as f:
        file_contest = f.read()
        return file_contest



print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
calculate_characters = number_of_characters(count_words(get_book_text(relative_path)))
print("--------- Character Count -------")
sorted_list_dictionary(calculate_characters)
print("============= END ===============")
