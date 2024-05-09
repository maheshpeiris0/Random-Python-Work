class book:
    def __init__(self,title,author,published_year):
        self.title = title
        self.author = author
        self.published_year = published_year
    
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Published Year: {self.published_year}")
        
        
book1 = book("The Alchemist","Paulo Coelho",1988)

book1.display()