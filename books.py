import PySimpleGUI as sg

selection = ""
currency = ""
price = 0

books = {
        "harry potter": {"price": price, "author": "JK Rowling"},
        "foundation": {"price": price, "author": "Isaac Asimov"},
        "game of thrones": {"price": price, "author": "George R. R. Martin"},
        "4 - lord of the rings": {"price": price, "author": "J. R. R. Tolkien"}
    }

window = sg.Window("Book Search")

while True:
    # This section is to choose whether you want to search or add a book
    layout1 = [
        [sg.Text("Please pick whether you want to add or search a book")],
        [sg.Button("Search"), sg.Button("Add"), sg.Button("Exit")]]
    
    window1 = sg.Window("Book Search", layout1)
    event1, values1 = window1.read()
    window1.close()

    # This section is to choose whether you want to search or add a book
    if event1 == "Search":
        layout2 = [
            [sg.Text("Enter the name of the book or the author to search:")],
            [sg.InputText(key="input")],
            [sg.Button("Search"), sg.Button("Exit")]] 
        window2 = sg.Window("Book Search", layout2)
        event2, values2 = window2.read()
        window2.close()

        # if the user clicks the "Exit" button or closes the window
        if event2 == sg.WIN_CLOSED or event2 == "Exit":
            break
        # if the user clicks the "Search" button
        if event2 == "Search":
            # get the user's input from the "input" element
            search_term = values2["input"]

    if search_term in books:
        layout4 = [
            [sg.Text("Please pick a region US, Indo, MY, EU")],
            [sg.Button("Malaysia"), sg.Button("USA"), sg.Button("Indonesia"), sg.Button("Europe"), sg.Button("Exit")]
        ]
        window4 = sg.Window("Book Search", layout4)
        event4, values4 = window4.read()
        window4.close()
    
        # if the user clicks the "Exit" button or closes the window
        if event4 == sg.WIN_CLOSED or event4 == "Exit":
            break

        # if the user clicks the "Malaysia" button
        if event4 == "Malaysia":
        
            # set the price based on the book title
            if search_term == "harry potter":
                price = 100
            elif search_term == "foundation":
                price = 20
            elif search_term == "game of thrones":
                price = 10
            elif search_term == "lord of the rings":
                price = 200
            book = books[search_term]
            sg.popup("Book found:", f"Title: {search_term}", f"Author: {book['author']}", f"Price: RM{price}")
        if event4 == "USA":
            # set the price based on the book title
            if search_term == "harry potter":
                price = 20
            elif search_term == "foundation":
                price = 100
            elif search_term == "game of thrones":
                price = 43
            elif search_term == "lord of the rings":
                price = 129
            book = books[search_term]
            sg.popup("Book found:", f"Title: {search_term}", f"Author: {book['author']}", f"Price: ${price}")
        if event4 == "Indonesia":
            # set the price based on the book title
            if search_term == "harry potter":
                price = 30000
            elif search_term == "foundation":
                price = 230000
            elif search_term == "game of thrones":
                price = 100000
            elif search_term == "lord of the rings":
                price = 50000
            book = books[search_term]
            sg.popup("Book found:", f"Title: {search_term}", f"Author: {book['author']}", f"Price: Rupiah{price}")
        if event4 == "Europe":
            # set the price based on the book title
            if search_term == "harry potter":
                price = 5
            elif search_term == "foundation":
                price = 10
            elif search_term == "game of thrones":
                price = 20
            elif search_term == "lord of the rings":
                price = 180
            book = books[search_term]
            sg.popup("Book found:", f"Title: {search_term}", f"Author: {book['author']}", f"Price: Euro{price}")
            # display the book details with the price
        else:
            # if the book is not found, display an error message
            sg.popup("Book not found.")
    elif event1 == "Add":
        layout3 = [
            [sg.Text("Enter the title of the book:")],
            [sg.InputText(key="title")],
            [sg.Text("Enter the author of the book:")],
            [sg.InputText(key="author")],
            [sg.Text("Enter the price of the book:")],
            [sg.InputText(key="price")],
            [sg.Button("Add"), sg.Button("Exit")]]
        window3 = sg.Window("Add Book", layout3)
        event3, values3 = window3.read()
        window3.close()
        
        # if the user clicks the "Exit" button or closes the window
        if event3 == sg.WIN_CLOSED or event3 == "Exit":
            break
        # if the user clicks the "Add" button
        if event3 == "Add":
            # get the user's input from the "input" elements
            title = values3["title"]
            author = values3["author"]
            price = values3["price"]

            # add the new book to the dictionary
            new_book = {"price": float(price), "author": author}
            books[title] = new_book
            sg.popup("Book added successfully!")        
    elif event1 == "Exit":
        break

# close the window when the loop is finished
sg.popup("Thanks for using the book search app!")
