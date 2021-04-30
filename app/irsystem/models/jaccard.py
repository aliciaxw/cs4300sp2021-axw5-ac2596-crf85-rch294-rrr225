from __future__ import division
import sys

# Jaccard is the intersection between two string diided by the set of two strings


def j_score(toks1, toks2):
    """
    [j_score(toks1, toks2)] is the jaccard similarity score for two lists of tokens,
    [toks1] and [toks2].

    Note:
      - assumes that [toks1] and [toks2] are not sets.
    """
    toks_1 = set(toks1)
    toks_2 = set(toks2)

    if len(toks_1) > 0 and len(toks_2) > 0:
        intersect = toks_1.intersection(toks_2)
        union = toks_1.union(toks_2)

        if len(union) == 0:
            return 0
        else:
            return len(intersect) / len(union)

    return 0

def query_to_jaccard_scores(query_dict, doc_toks):
    """
    Given a query dict from search_controller.py and a document list of attributes, return the jaccard score.
    This function acts as a helper to extract attributes and keywords from the query dict.
    """
    query_toks = []

    for attr in query_dict.keys():
        if attr == 'search':
            # handle other trail attributes
            if "wildlife" in attr:
                query_toks.append("Unique Wildlife Viewing")
            if "picnic" in attr:
                query_toks.append("Picnicking allowed")
            if "scenic" in attr:
                query_toks.append("Scenic Vistas")
        if attr == 'difficulty':
            query_toks.append(query_dict['difficulty'])

        if attr == 'requireFreeEntry':
            query_toks.append("No fee")
        if attr == 'requireRestrooms':
            query_toks.append("Restrooms available")

        if attr == 'walkOn':
            pass
        if attr == 'hikeOn':
            query_toks.append("Good for Hiking")
        if attr == 'runOn':
            query_toks.append("Good for Running")
        if attr == 'bikeOn':
            query_toks.append("Good for Biking")
        if attr == 'horseOn':
            query_toks.append("Good for Horseback Riding")
        if attr == 'swimOn':
            pass
        if attr == 'skiOn':
            query_toks.append("Good for Cross-Country Skiiing")
        if attr == 'snowshoeOn':
            query_toks.append("Good for Snowshoeing")

    return j_score(query_toks, doc_toks)


def get_jaccard_scores(query_dict, data):
    """
    Returns a dictionary of trail name to jaccard score based on trail attributes
    including activity types, difficulty, and accessibility (except wheelchair).
    """
    out = {}
    for trail_name in data.keys():
        trail_attributes = data[trail_name]['Trail Attributes'] + [data[trail_name]['Difficulty']]
        out[trail_name] = query_to_jaccard_scores(query_dict, trail_attributes)
    
    return out

# def test():
#     t1 = ['hello', 'world']
#     t2 = ['hello', 'a']
#     t3 = []
#     t4 = ['a', 'b', 'c ']
#     t5 = ['a', 'c', 'b', ' ']
#     print(j_score(t1, t1))
#     print(j_score(t1, t2))
#     print(j_score(t3, t3))
#     print(j_score(t4, t1))
#     print(j_score(t4, t5))


# if __name__ == '__main__':
#     test()
