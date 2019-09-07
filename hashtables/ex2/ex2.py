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
    hashtable = HashTable(length*2) #initialize it twice to make access faster
    route = [None] * length

    """
    YOUR CODE HERE...
    By looping over the array, we add the ticket to the hash table
    """
    #Insert each ticket into the hashtable
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    
    #    
    route[0] = hash_table_retrieve(hashtable, 'NONE')
    
    #Hint: Map values in the hash table
    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route
