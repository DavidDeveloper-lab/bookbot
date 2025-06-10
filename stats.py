def count_words(text_book: str) -> list[str]:
    words_list = text_book.split()
    count = 0
    for i in range(0, len(words_list)):
        count += 1
    print(f"{count} words found in the document")
    return (words_list)

def number_of_characters(text_string: list[str]) -> dict:
    count_dictionary = {}
    for i in range(0, len(text_string)):
         for j in range(0, len(text_string[i])):
            if text_string[i][j].lower() in count_dictionary:
                count_dictionary[text_string[i][j].lower()] += 1
            else:
                count_dictionary[text_string[i][j].lower()] = 1       

    return count_dictionary

def obtain_value(value):
    """This function returns the value of the characters for the sorted_list_dictionary function"""
    return value["num"]

def sorted_list_dictionary(dictionary) -> list[dict]:
    sorted_list = []
    for key, value in dictionary.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        sorted_list.append(new_dict)
        sorted_list.sort(reverse=True, key=obtain_value)
    print(sorted_list)
    
    
    