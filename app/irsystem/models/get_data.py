import pprint
import json

with open('ithacatrails.json') as f:
    data = json.load(f)

def get_trail_to_idx():
    trail_to_id = {}
    for i, trail in enumerate(data):
        trail_to_id[trail] = i
    return trail_to_id

def get_idx_to_trail_name(trail_to_idx_dict):
    return {value:key for key, value in trail_to_idx_dict.items()}

def get_distance_list():
    return sorted([(name, data[name]['Distance']) for name in data], key = lambda x: x[1])


NUM_DOCS = len(data)

# trail to index
trail_to_idx = get_trail_to_idx()

# trail index to trail name
idx_to_trail_name = get_idx_to_trail_name(trail_to_idx)

# List of trail names
trail_names = [trail for trail in data]

distance_list = get_distance_list()

# print(max(distance_list, key = lambda x: x[1]))
