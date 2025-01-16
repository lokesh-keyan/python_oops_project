class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secretAttr = "secret attributr" # double underscore makes the attribute private
    
    def getprice(self):
        if hasattr(self, "_discount"): # in-built function to check if the object has the attribute
            return self.price - (self.price * self._discount)
        return self.price

    def setdiscount(self, amount):
        self._discount = amount # the underscore exists only in the class 

book1 = Book("Richest man in Babylon", "George S. Clason", 191, 9.99)
print(book1)
book1.setdiscount(0.5)
print(book1.getprice())

print(book1.__secretAttr) # this will throw an error as the attribute is private
print(book1._Book__secretAttr) # this will print the value of the attribute, its more like static method in c#