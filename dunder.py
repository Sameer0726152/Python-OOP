class Library:
    def __init__(self, name, books):
        self.name = name
        self.books = books

    def __str__(self):
        return f"Library: {self.name} | {len(self.books)} books"

    def __repr__(self):
        return f"Library(name={self.name!r}, books={self.books!r})"

    def __len__(self):
        return len(self.books)

    def __contains__(self, item):
        return item in self.books 

    def __getitem__(self, key):
        return self.books[key]

    def __add__(self, other):
        merged_name = f"{self.name} & {other.name}"
        merged_books = self.books + other.books
        return Library(merged_name, merged_books)

    def __eq__(self, other):
        return self.books == other.books
    
l1 = Library("SAM", ["Python Basics", "Clean Code", "DSA"])
l2 = Library("NIHAR", ["AI Fundamentals", "Deep Learning", "System Design"])

print(l1)
print(repr(l2))
print(len(l1))
print("SAM" in l1)
print(l2[1])
print(l1 + l2)
print(l1 == l2)