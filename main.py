def main():
    file_contents = get_book_contents("frankenstein")
    report_maker(file_contents)

def get_book_contents(book_name):
    with open(f"books/{book_name}.txt") as f:
        file_contents = f.read()
    return file_contents

def word_counter(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    char_dict = {}
    lowered_contents = file_contents.lower()
    for i in lowered_contents:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict

def listing_part_of_report(file_contents):
    char_dict = count_characters(file_contents)
    for i in char_dict:
        if i.isalpha():
            print(f"The '{i}' character was found {char_dict[i]} times ")


def report_maker(file_contents):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_counter(file_contents)} words found in the document \n")
    listing_part_of_report(file_contents)
    print("--- End report ---")
main()
