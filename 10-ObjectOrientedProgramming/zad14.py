class Ebook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
        self.if_open = False

    def open_book(self):
        self.if_open = True

    def next_page(self):
        if self.current_page < self.pages and self.if_open:
            self.current_page += 1

    def previous_page(self):
        if self.current_page > 0 and self.if_open:
            self.current_page -= 1


book = Ebook("Hobbit", "James X", 120)
print(book.current_page)
book.next_page()
print(book.current_page)
book.next_page()
book.open_book()
print(book.current_page)
book.next_page()
book.next_page()
book.next_page()
book.next_page()
book.previous_page()
print(book.current_page)
