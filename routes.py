from Route import Route
from pages import homepage, about

route = Route()

route.add_route(homepage, "/")
route.add_route(about, "/about")

class Base_Route(Route):
    pass


def get_routes(app):
    pass


