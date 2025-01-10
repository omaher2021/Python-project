from tkinter import *
from tkinter import messagebox

# Creating Node Class
class Node:
    def __init__(self, bookid, name, cost, author, quantity, bound):
        self.bookid = bookid
        self.name = name
        self.cost = cost
        self.author = author
        self.quantity = quantity
        self.bound = bound
        self.next = None

# Linked List Data Structure for managing bookstore operations
class LinkedList:
    def __init__(self):
        self.head = None

    def add_book(self, bookid, name, cost, author, quantity, bound):
        new_book = Node(bookid, name, cost, author, quantity, bound)
        if not self.head:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        messagebox.showinfo("Success", "Book added successfully!")

    def remove_book_by_name(self, key):
        curr = self.head
        prev = None
        while curr:
            if curr.name.lower() == key.lower():
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                messagebox.showinfo("Success", f"Book '{key}' removed successfully.")
                return
            prev = curr
            curr = curr.next
        messagebox.showerror("Error", f"Book '{key}' not found!")

    def print_list(self):
        books = []
        temp = self.head
        while temp:
            books.append(f"Book ID: {temp.bookid}, Name: {temp.name}, Cost: {temp.cost}, "
                         f"Author: {temp.author}, Quantity: {temp.quantity}, Bound: {temp.bound}")
            temp = temp.next
        if books:
            messagebox.showinfo("Book List", "\n".join(books))
        else:
            messagebox.showinfo("Book List", "No books available.")

    def search_book(self, key, by="name"):
        temp = self.head
        found = False
        while temp:
            if (by == "name" and temp.name.lower() == key.lower()) or \
               (by == "id" and temp.bookid == key) or \
               (by == "author" and temp.author.lower() == key.lower()):
                messagebox.showinfo("Book Found", 
                                    f"Book ID: {temp.bookid}, Name: {temp.name}, Cost: {temp.cost}, "
                                    f"Author: {temp.author}, Quantity: {temp.quantity}, Bound: {temp.bound}")
                found = True
                break
            temp = temp.next
        if not found:
            messagebox.showerror("Error", "Book not found!")

# Bookstore GUI Application
class BookstoreApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bookstore Management System")
        self.linked_list = LinkedList()
        self.setup_ui()

    def setup_ui(self):
        Label(self.master, text="Bookstore Management System", font=("Arial", 18)).pack(pady=10)

        Button(self.master, text="Add Book", command=self.add_book_ui, width=20).pack(pady=5)
        Button(self.master, text="Remove Book", command=self.remove_book_ui, width=20).pack(pady=5)
        Button(self.master, text="Search Book", command=self.search_book_ui, width=20).pack(pady=5)
        Button(self.master, text="Display All Books", command=self.display_books, width=20).pack(pady=5)
        Button(self.master, text="Exit", command=self.master.quit, width=20).pack(pady=5)

    def add_book_ui(self):
        add_window = Toplevel(self.master)
        add_window.title("Add Book")

        Label(add_window, text="Book ID").grid(row=0, column=0, padx=5, pady=5)
        Label(add_window, text="Name").grid(row=1, column=0, padx=5, pady=5)
        Label(add_window, text="Cost").grid(row=2, column=0, padx=5, pady=5)
        Label(add_window, text="Author").grid(row=3, column=0, padx=5, pady=5)
        Label(add_window, text="Quantity").grid(row=4, column=0, padx=5, pady=5)
        Label(add_window, text="Bound").grid(row=5, column=0, padx=5, pady=5)

        bookid = Entry(add_window)
        name = Entry(add_window)
        cost = Entry(add_window)
        author = Entry(add_window)
        quantity = Entry(add_window)
        bound = Entry(add_window)

        bookid.grid(row=0, column=1, padx=5, pady=5)
        name.grid(row=1, column=1, padx=5, pady=5)
        cost.grid(row=2, column=1, padx=5, pady=5)
        author.grid(row=3, column=1, padx=5, pady=5)
        quantity.grid(row=4, column=1, padx=5, pady=5)
        bound.grid(row=5, column=1, padx=5, pady=5)

        def add_book():
            try:
                self.linked_list.add_book(
                    int(bookid.get()), name.get(), float(cost.get()), author.get(), int(quantity.get()), bound.get()
                )
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please check your entries.")

        Button(add_window, text="Add", command=add_book).grid(row=6, columnspan=2, pady=10)

    def remove_book_ui(self):
        remove_window = Toplevel(self.master)
        remove_window.title("Remove Book")

        Label(remove_window, text="Enter Book Name to Remove").pack(pady=5)
        name = Entry(remove_window)
        name.pack(pady=5)

        def remove_book():
            self.linked_list.remove_book_by_name(name.get())
            remove_window.destroy()

        Button(remove_window, text="Remove", command=remove_book).pack(pady=5)

    def search_book_ui(self):
        search_window = Toplevel(self.master)
        search_window.title("Search Book")

        Label(search_window, text="Search By").grid(row=0, column=0, padx=5, pady=5)
        Label(search_window, text="Key").grid(row=1, column=0, padx=5, pady=5)

        search_by = StringVar(value="name")
        Radiobutton(search_window, text="Name", variable=search_by, value="name").grid(row=0, column=1)
        Radiobutton(search_window, text="ID", variable=search_by, value="id").grid(row=0, column=2)
        Radiobutton(search_window, text="Author", variable=search_by, value="author").grid(row=0, column=3)

        key = Entry(search_window)
        key.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        def search_book():
            try:
                search_key = int(key.get()) if search_by.get() == "id" else key.get()
                self.linked_list.search_book(search_key, by=search_by.get())
                search_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please check your entries.")

        Button(search_window, text="Search", command=search_book).grid(row=2, columnspan=4, pady=10)

    def display_books(self):
        self.linked_list.print_list()

if __name__ == "__main__":
    root = Tk()
    app = BookstoreApp(root)
    root.mainloop()
