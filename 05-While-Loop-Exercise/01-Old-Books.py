book_name = input()

book_count = 0
is_book_found = False

while True:
    current_book = input()

    if current_book == "No More Books":
        break

    if current_book == book_name:
        is_book_found = True
        print(f"You checked {book_count} books and found it.")
        break

    book_count += 1

if not is_book_found:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")
