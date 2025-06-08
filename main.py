from stats import count_words
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
count_words(get_book_text(relative_path))