def main():
    filepath = "books/frankenstein.txt"
    text = get_file(filepath)
    words, letters = count_words(text)

    list_letters = convert_dict_to_list(letters)

    list_letters.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    for item in list_letters:
        print(f"The {item["letter"]} was found {item["times"]} times")
    print("--- End report ---")

def get_file(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["times"]

def convert_dict_to_list(dict):
    list = []
    for letter in dict:
        list.append({"letter": letter, "times": dict[letter]})

    return list


def count_words(text):
    counter = 0
    letters = {}
    for word in text.split():
        lower_word = word.lower()
        for letter in lower_word:
            if not letter.isalpha():
                continue
            elif letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        counter += 1
    return counter, letters

main()