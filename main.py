from stats import count_words, number_of_characters, sorted_list_dictionary
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

calculate_characters = number_of_characters(count_words(get_book_text(relative_path)))
sorted_list_dictionary(calculate_characters)
