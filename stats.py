def count_words(text_book: str) -> list[str]:
    """This function takes a string and returns the number of words that it has"""
    words_list = text_book.split()
    count = 0
    for i in range(0, len(words_list)):
        count += 1
    print(f"Found {count} total words")
    return (words_list)

def number_of_characters(text_string: list[str]) -> dict:
    """This function take a list of strings and returns a dictionary with key, values formated this way: 'char': number of times the character showed up in the string. """
    count_dictionary = {}
    for i in range(0, len(text_string)):
         for j in range(0, len(text_string[i])):
            if text_string[i][j].lower() in count_dictionary:
                count_dictionary[text_string[i][j].lower()] += 1
            else:
                count_dictionary[text_string[i][j].lower()] = 1       

    return count_dictionary

def obtain_value(value: dict):
    """This function returns the value of the characters for the sorted_list_dictionary function"""
    return value["num"]

def sorted_list_dictionary(dictionary: dict) -> list[dict]:
    """This function takes a dictionary and prints a list with dictionaries. For each indexes, the dictionaries have this format: 'char':character, 'num': number of characters that were found in the book """
    sorted_list = []
    for key, value in dictionary.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        sorted_list.append(new_dict)
        sorted_list.sort(reverse=True, key=obtain_value)
    for i in range(len(sorted_list)):
        if sorted_list[i]['char'].isalpha():
            print(f"{sorted_list[i]['char']}: {sorted_list[i]['num']} ")


    

