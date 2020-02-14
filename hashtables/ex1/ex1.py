#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
# start with the length of weights
    for index in range(length):
# check the difference between the limit and each weight
        diff = limit - weights[index]
# add more weights to table
# find which weights hit the limit
        target = hash_table_retrieve(ht, diff)
# if the target isn't empty find the index of the element needed to bring the sum to the limit
        if target is not None:
            return(index, target)
# store the weights in the hashtable
        hash_table_insert(ht, weights[index], index)
    return None



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
