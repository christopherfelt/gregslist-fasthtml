from fasthtml.common import *
import inspect

class Page:
    
    def __init__(self, route, app):
        app.get(route, self.page())
        
        # you would have a wrapper or some funciton that would upon instantiation build and apply the routes to the app object
        # you would need to see the contents of the page loop through all of its components and then
        
        page_lines = inspect.getsource(self.page).splitlines()
        for line in page_lines:
            # then look at each line to see if it includes an hx_ http method
            # then it finds the function within the class
            # then it adds it to the route with the hx http method
            
            http_method = "get"
            getattr(app, http_method)(url, function)
            pass
    
    def get_page(self):
        return self.page()
    
    def page(self):
        Div("Hello World")
        


class Homepage(Page):
    
    def page(self):
        Div("Hello from Homepage",
                A("About", hx_get="/about"), 
                Button("Change the text", hx_get="/change_text", hx_target="#homepage-div"),
                id="homepage-div")
        

    def change_text(self): #you would set the name of the function to the hx_get url. But what about params?
        return "new text"