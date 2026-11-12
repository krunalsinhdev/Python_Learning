# Magic (Dunder) Methods
# Special methods such as __str__ and __len__ customize object behavior.

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __len__(self):
        return self.pages

book = Book("Learn Python", 250)
print(book)          # Calls book.__str__()
print("Pages:", len(book))  # Calls book.__len__()
