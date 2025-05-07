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