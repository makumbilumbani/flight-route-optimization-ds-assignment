# Class to validate the airport input
class Validator:
    def get_valid_starting_airport(graph):
            all_airports = graph.get_all_airports()
            
            while True:
                starting_airport = input("Enter the starting airport (e.g., 'DSM'): ").strip().upper()
                if starting_airport in all_airports:
                    return starting_airport
                else:
                    print(f"Error: '{starting_airport}' is not available in the list of routes. Please try again.")

