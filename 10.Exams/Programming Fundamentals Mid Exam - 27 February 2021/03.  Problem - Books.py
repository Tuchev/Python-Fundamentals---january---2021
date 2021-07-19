books = input().split("&")
command = input()

while not command == "Done":
    commands = command.split(" | ")
    name = commands[0]
    book_name = commands[1]
    if name == "Add Book":
        if book_name not in books:
            books.insert(0, book_name)
    elif name == "Take Book":
        if book_name in books:
            books.remove(book_name)
    elif name == "Swap Books":
        book_new = commands[2]
        if book_name in books and book_new in books:
            index_book = books.index(book_name)
            index_new = books.index(book_new)
            books[index_book], books[index_new] = books[index_new], books[index_book]
    elif name == "Insert Book":
        books.append(book_name)
    elif name == "Check Book":
        index = int(book_name)
        if index in range(len(books)):
            print(f"{books[index]}")
    command = input()
if command == "Done":
    print(f"{', '.join(books)}")