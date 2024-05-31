# Python Data Structure Challenges in Real-world Scenerios

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def book_checker(inventory, book):  
        if book in inventory:
            return f"This book is already in stock"
        else:
            book_stat = list(inventory)
            book_stat.append(book)
            inventory = tuple(book_stat)
        return inventory

user_book = input("What book are you looking for? ").title()
user_author = input("Whose the author of the book? ").title()
print(book_checker(library, (user_book, user_author)))
