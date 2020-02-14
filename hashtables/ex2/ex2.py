#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []
    count = 0

    """
    YOUR CODE HERE
    """

# store all the tickets in the hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
# we know the starting location has a source of NONE
    city = hash_table_retrieve(hashtable, "NONE")
# now we loop through
    while city != "NONE":
        route.insert(count, city)
        count += 1
        new_city = hash_table_retrieve(hashtable, city)
        city = new_city
    return route