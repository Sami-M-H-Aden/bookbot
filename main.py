def main():
    file_contents = get_book_contents("frankenstein")
    num_words = word_counter(file_contents)
    print(f"{num_words} words were found in the document")
    print(count_characters(file_contents))

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
    lowered_contents = lowered_contents.split()
    for i in lowered_contents:
        for j in i:
            if j in char_dict:
                char_dict[j] += 1
            else:
                char_dict[j] = 1
    return char_dict


main()
