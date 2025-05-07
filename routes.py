from Route import Route
from pages import homepage, about

route = Route()

route.page_route(homepage, "/")
route.page_route(about, "/about")

class Base_Route(Route):
    pass


def get_routes(app):
    pass


