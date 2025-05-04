from fasthtml.common import *

app, rt = fast_app()

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
                Li(A("Cars", href="/cars")),
                Li(A("House", href="/house"))
            )
        ),
        Div(
            P("hello world!", style='text-align: center'), 
            # style="border: 2px solid black; padding: 10px;"
        ),
        Div(
            Card(
                "Stuff Stuff"
                # Header("I'm a header"),
                # "Body",
                # Footer("I'm a footer"),
            ),
            Card(
                "stuff stuff stuff"
            )
        ),
        style="width: 35%; margin: 0 auto;",
        
    )


@rt('/cars')
def get():
    return Div("Made it to cars")



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


# def get():
#     return Container(
#         Grid(
#             Div(),
#             Div(
#                 Nav(
#                     Ul(
#                         Li(
#                             Strong("Gregslist")
#                         )
#                     ),
#                     Ul(
#                         Li(A("Cars", href="/cars")),
#                         Li(A("House", href="/house"))
#                     )
#                 )
#             ),
#             Div()
#         ),
#         Grid(
#             Div(),
#             Div(
#                 P("hello world!"), 
#                 style="border: 2px solid black; padding: 10px;"
#             ),
#             Div()
#         ),
#         Card(
#             Header("I'm a header"),
#             "Body",
#             Footer("I'm a footer"),
#             style="width: 50%; margin: 0 auto;"
#         )
        
#     )