def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    words_count = book_word_count(text)
    print(f"{book_path} has {words_count} words")
    character_dict = book_character_count(text)
    #print(character_dict)
    #dict_list = dict_to_list(character_dict)
    (dict_to_list(character_dict))
    


def book_character_count(text):
    text_lower = text.lower()   #make text to lower case
    char_dict = {}
    for char in text_lower:
        if char not in char_dict.keys():
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(item):
    # Gets the first value from the dictionary
    return list(item.values())[0]

def dict_to_list(dict):
    dlist = []
    for k, v in dict.items():
        if k.isalpha():
            dlist.append({k: v})
    dlist.sort(reverse=True, key=sort_on)

    for p in dlist:
        # Get the first (and only) key-value pair from the dictionary
        character = list(p.keys())[0]
        count = list(p.values())[0]
        print(f"The '{character}' character was found {count} times")

    


#open text file and return text as string
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
#splits the string by spaces, return length of string
def book_word_count(text):
    words = text.split()
    return len(words)
main()