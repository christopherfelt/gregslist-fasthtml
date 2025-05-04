from fasthtml.common import *
from models import car_table, house_table

app, rt = fast_app()

# TODO

# add all the crud stuff

def demo_cards():
    stuff_content = ["stuff", "things"]
    
    return Div(*[Card(stuff) for stuff in stuff_content])


@rt('/')
def get():
    return Container(
        Nav(
            Ul(
                Li(
                    H1("Gregslist")
                )
            ),
            Ul(
                Li(A("Cars", hx_get="/cars", hx_target="#item-list")),
                Li(A("House", href="/house"))
            )
        ),
        Div(demo_cards(), id="item-list"),
        
        style="width: 35%; margin: 0 auto;",
        
    )


@rt('/cars')
def get():
    cars = car_table()
    return list_with_new_button(cars,"description")
    # return Div(*[Card(f"{car.description}") for car in cars])


def list_with_new_button(list_items, display_field:str):
    cards = [Card(f"{getattr(item, display_field)}") for item in list_items]
    return Div(
        *cards,
        Button("Add")
    )


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