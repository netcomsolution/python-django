class Books:
    def __init__(self,a,b):
        self.a = a
        self.b = b 

    def english_book(self):
        return self.a+self.b
            
    def farshi_book(self):
        return self.a-self.b
            

english_book = Books(20,10)
farshi_book = Books(20,10)

print(english_book.english_book())
print(farshi_book.farshi_book())