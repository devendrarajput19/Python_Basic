class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.issued_copy = 0
        self.is_available = True
        self.issued_to = []

    def issue_book(self, member_name):
        if not self.is_available:
            print(f"{self.title} is not available...")
            print(f"{self.total_copies} copies are issued out...")
        elif member_name in self.issued_to:
            print(f"{member_name} has already issued to {self.title}")
        else:
            self.issued_copy += 1
            self.issued_to.append(member_name)
            available_now = self.total_copies - self.issued_copy

            if available_now == 0:
                self.is_available = False
            
            print(f" '{self.title}' issued to {member_name} successfully!")
    
    def check_status(self):
        available_now = self.total_copies - self.issued_copy

        print(f"Book ID      : {self.book_id}")
        print(f" Title        : {self.title}")
        print(f"Author       : {self.author}")
        print(f"Total Copies : {self.total_copies}")
        print(f"Issued       : {self.issued_copy}")
        print(f"Available    : {available_now}")

book1 = Book("B001", "Python Basics", "Guido van Rossum", 3)

book1.issue_book("Rohan Mehta")       
book1.issue_book("Priya Patel")
book1.check_status()

