
class book:

    def __init__(self, title, author, stock):
        self.title = title
        self.author = author
        self.stock = stock

    def display_book(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")

        if self.stock >= 1:
            print("Status : Available")
        else:
            print("Status : Not available")

    def issue_book(self):
        if self.stock >= 1:
            print(f"{self.title} issued successfully")
            self.stock -= 1
        else:
            print(f"{self.title} Not available")

    def return_book(self):
        self.stock += 1
        print(f"{self.title} Returned Successfully")

book1  = book("math", "RD", 3)
book2 = book("Science", "HS", 3)
book3 = book("English", "DR SIR", 8)

book1.display_book()
book1.issue_book()
book1.return_book()
book1.issue_book()




