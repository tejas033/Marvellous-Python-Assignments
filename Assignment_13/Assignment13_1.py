# OOPs demo :: BookStore

class BookStore:
    NoOfBooks = 0                       # Class variable, access this using class name out side instace methods

    def __init__(self, name, author):
        self.Name = name                # Instance variables
        self.Author = author

    def Display(self):
        print(f'Name of book: {self.Name} by {self.Author}, NoOfBooks: {BookStore.NoOfBooks}')          # BookStore.NoOfBooks or self.NoOfBooks both will return current value of Class variable

def main():
    obj1 = BookStore('Linux System Programming', 'Robert Love')
    BookStore.NoOfBooks += 1
    obj1.Display()
    
    obj2 = BookStore('C Programming', 'Dennis Ritchie')
    BookStore.NoOfBooks += 1
    obj2.Display()

if __name__ == "__main__":
    main()