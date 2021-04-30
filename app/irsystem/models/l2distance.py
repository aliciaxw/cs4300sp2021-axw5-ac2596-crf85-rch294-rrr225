from app.irsystem.models.get_data import distance_list
import numpy as np

def get_l2_distance(query_distance):
    query_distance = int(query_distance)
    rankings = {}
    for tup in distance_list:
        if tup[1] <= query_distance:
            rankings[tup[0]] = 1
        else:
            rankings[tup[0]] = 1/(100*np.linalg.norm(query_distance - tup[1]))
    return rankings