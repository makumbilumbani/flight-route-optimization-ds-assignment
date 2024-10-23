from classes.graph import Graph
from classes.routeOptimizer import RouteOptimizer
from classes.validator import Validator

if __name__ == "__main__":
    # Creating an instance of the graph class
    flight_graph = Graph()

    # populating routes based on the airport routes
    routes = [
        ('DSM', 'ORD'), ('ORD', 'BGI'), ('BGI', 'LGA'), ('LGA', 'ORD'),
        ('SFO', 'SAN'), ('SAN', 'EYW'), ('EYW', 'SAN'), ('LHR', 'SFO'),
        ('TLV', 'DEL'), ('DEL', 'DOH'), ('DOH', 'CDG'), ('CDG', 'BUD'),
        ('CDG', 'DEL'), ('SIN', 'CDG'), ('HND', 'ICN'), ('ICN', 'JFK'),
        ('JFK', 'HND'), ('EWR', 'HND')
    ]

    for u, v in routes:
        flight_graph.add_route(u, v)

    # Setting the starting airport
    # Getting valid starting airport from console input
    starting_airport = Validator.get_valid_starting_airport(flight_graph)

    # Creating the route optimizer and calculating the minimum additional routes
    optimizer = RouteOptimizer(flight_graph, starting_airport)
    result = optimizer.minimum_additional_routes()

    print(f"Minimum number of additional routes needed: {result}")