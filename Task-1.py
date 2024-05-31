# Tuple Mastery in Python

def flight_details(detail):
    flight_info = ""
    for num, passenger in enumerate(detail):
       name, origin_location, destination = passenger
       flight_info += f"Itinerary {num + 1}: {name} - From {origin_location} to {destination}\n"
    return flight_info   

print(flight_details([("Jessie", "Tokyo", "New York"), ("John", "California", "Boston")]))
