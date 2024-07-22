def main():
    file_contents = get_book_contents("frankenstein")
    word_count = word_counter(file_contents)

def get_book_contents(book_name):
    with open(f"books/{book_name}.txt") as f:
        file_contents = f.read()
    return file_contents

def word_counter(file_contents):
    words = file_contents.split()
    return len(words)

main()
