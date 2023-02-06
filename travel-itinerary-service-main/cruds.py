# Itinerary Cruds

def sql_insert_travel(itinerary_id, review_id, origin, destination, origin_code, \
        destination_code, departure_time, arrival_time, airline_name, flight_num, cost):
    return f'INSERT INTO Travel(itinerary_id, review_id, origin, destination, origin_code, destination_code, departure_time, arrival_time, airline_name, flight_num, cost) VALUES ({itinerary_id},{review_id},{origin},{destination},{origin_code},{destination_code},{departure_time},{arrival_time},{airline_name},{flight_num},{cost})'

def sql_select_travel_itinerary_id(itinerary_id):
    return f'SELECT * FROM Travel where itinerary_id = {itinerary_id}'


def sql_update_travel(origin, destination, origin_code, destination_code, travel_id):
    return f'UPDATE Travel SET origin="{origin}", destination="{destination}", origin_code={origin_code}, destination_code={destination_code} WHERE travel_id={travel_id}'


def sql_delete_travel_by_id(travel_id):
    return f'DELETE from Travel WHERE travel_id={travel_id}'
