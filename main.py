from stats import *
relative_path = "books/frankenstein.txt"


def get_book_text(filepath):
    with open(filepath) as f:
        file_contest = f.read()
        return file_contest
"""
def main():
    print(get_book_text(relative_path))
"""


###main()
print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
calculate_characters = number_of_characters(count_words(get_book_text(relative_path)))
print("--------- Character Count -------")
sorted_list_dictionary(calculate_characters)
print("============= END ===============")
