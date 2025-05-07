from fasthtml.common import *
from models import car_table, house_table, job_table

app, rt = fast_app()

# TODO

# add all the crud stuff
# need a way to differentiate within page changes and entire pages



@rt('/')
def get():
    return get_home_page()


@rt('/cars')
def get():
    cars = car_table()
    return list_with_new_button(cars,"description")

@rt('/new/{record_class}')
def get(record_class:str):
    return new_post_form(record_class)


# pages
def get_home_page():
    nav_bar = nav_bar()
    style = "width: 35%; margin: 0 auto;"
    return Container(
        nav_bar,   
        Div(demo_cards(), id="item-list"),
        style=style,
        
    )

# components
def nav_bar():
    return Nav(
                Ul(
                    Li(
                        H1("Gregslist")
                    )
                ),
                Ul(
                    Li(A("Cars", hx_get="/cars", hx_target="#item-list")),
                    Li(A("House", href="/house"))
                )
            )

def demo_cards():
    stuff_content = ["stuff", "things"]
    return Div(*[Card(stuff) for stuff in stuff_content])

def list_with_new_button(list_items, display_field:str):
    cards = [Card(f"{getattr(item, display_field)}") for item in list_items]
    record_class = get_class_name_from_record(list_items[0])
    return Div(
        *cards,
        Button("Add", hx_get="/new/"+record_class, hx_target="#item-list")
    )

def new_post_form(record_class:str):
    inner_text = "testing " + record_class
    return Div(inner_text)


# utilities
def get_class_name_from_record(record):
    return str(type(record).__name__.lower())
    
# def add_parameter(func):
#     params = []
#     def wrapper(*new_args):
#         nonlocal params
#         if new_args:
#             params.extend(new_args)
#             return wrapper
#         else:
#             return func(*params)
#     return wrapper

# @add_parameter
# def get_nav():
#     nav = Nav
    

    
serve()