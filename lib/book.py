#!/usr/bin/env python3

class Book:
    pass
    def __init__(self,title,page_count):
        self.title = title
        self.page_count = page_count
    
    def get_page(self):
        return self._page_count

    def set_page(self,page_count):
        if type(page_count) is (int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    
    page_count = property(get_page,set_page)  
        
           
        