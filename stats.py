def count_words(text_book):
    words_list = text_book.split()
    count = 0
    for i in range(0, len(words_list)):
        count += 1
    print(f"{count} words found in the document")
    return (words_list)

def number_of_characters(text_string):
    count_dictionary = {}
    for i in range(0, len(text_string)):
        for j in range(0, len(text_string[i])):
            if text_string[i][j].lower() in count_dictionary:
                count_dictionary[text_string[i][j].lower()] += 1
            else:
                count_dictionary[text_string[i][j].lower()] = 1       

    print(count_dictionary)