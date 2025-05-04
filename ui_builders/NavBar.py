from fasthtml.common import *
import random
import string

class NavBar:
    
    def __init__(self):
        self.base_nav_container = {};
    
    def add_element(self, element):
        id = self.generate_id()
        self.base_nav_container[id] = element
        return id

    def add_elements(self, elements):
        ids = []
        for element in elements:
            ids.append(self.add_element(element))
        
        return ids
            
    
    def generate_id():
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters, k=8))
    
    

navBar = NavBar()

navBar.Ul(id="website-name").Li(H1("Gregslist"))
navBar.Ul().Li(A("Cars", href="/cars")).getParent().Li(A("House", href="/house"))


