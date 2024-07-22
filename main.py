def main():
    file_contents = get_book_contents("frankenstein")
    print(file_contents)
def get_book_contents(book_name):
    with open(f"books/{book_name}.txt") as f:
        file_contents = f.read()
    return file_contents


main()
