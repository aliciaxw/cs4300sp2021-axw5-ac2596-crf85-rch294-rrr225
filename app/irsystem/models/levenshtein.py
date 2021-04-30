import sys
import numpy as np
# from get_data import datas
import pprint


"""
Notes:
    Problem 1:
        Trails which do not have the "-" might be unevenly calculated.
    
    Problem 2:
        How to differentiate between sub-trails. Still penalizes longer strings.
"""


def insert_cost(source, j):
    """
    Returns the current insertion cost of inserting the [j]-th character of the
    source word.
    """
    # does not penalize for the word appearing in the middle of the query
    return 0


def delete_cost(target, i):
    """
    Returns the current deletion cost of deleting the [i]-th character of the
    [target] word.
    """
    return 2


def substitute_cost(target, source, i, j):
    """
    Returns the current substitution cost of substituting the [i]-th character
    of the [target] word with the [j]-th character of the [source] word.
    """
    if target[i - 1] == source[j - 1]:
        return 0
    else:
        return 2


# Setting custom operation costs
curr_delete_function = delete_cost
curr_insert_function = insert_cost
curr_substitute_function = substitute_cost


def lev_mat(target, source):
    """
    Calculates the edit-distance matrix where the cell [i, j] corresponds to
    the edit-cost (under) custom parameters) of transforming the first i letters
    of the target to the first j letters of the source.

    * As calculated in A3 *
    """
    m = len(target) + 1
    n = len(source) + 1

    matrix = np.zeros((m, n))
    for i in range(1, m):
        matrix[i, 0] = matrix[i-1, 0] + curr_delete_function(target, i)

    for j in range(1, n):
        matrix[0, j] = matrix[0, j-1] + curr_insert_function(source, j)

    for i in range(1, m):
        for j in range(1, n):
            matrix[i, j] = min(
                # "down" or delete op
                matrix[i-1, j] + curr_delete_function(target, i),
                # "right" or insert op
                matrix[i, j-1] + curr_insert_function(source, j),
                # "diagonal" or sub op
                matrix[i-1, j-1] + \
                curr_substitute_function(target, source, i, j)
            )

    return matrix


def levenshtein(target, source):
    """
    Calculates the levenshtein ditance between the source string and target
    string.
    """
    m = lev_mat(target, source)
    return m[len(target), len(source)]


def ranked_levs(target, sources):
    """
    Returns a dictionary {trail_name: score} of the
    [sources] as calculated by the levenshtein() function above.

    Note:
    Because there are often multiple trails with the same park name,
    and the Levenshtein edit-distance penalizes strings longer than
    the query, I have split the string at the '-' which signals a 
    sub-trail. Therefore:
        Edwards Lake Cliiffs Trail - Pocket Falls
            --> Edwards Lake Cliiffs Trail
    """
    edit_distance_rankings = {}

    for trail in sources:
        source = trail
        edit_cost = levenshtein(target, source.split(' - ', 1)[0])
        edit_cost = 1 if edit_cost == 0 else edit_cost  # avoid divide by zero
        edit_distance_rankings[source] = 1 / edit_cost

    return edit_distance_rankings

# Code for testing:

# def test():
#     trails = [trail for trail in data]
#     ranks = ranked_levs('Lindsay-Parsons', trails)
#     pp = pprint.PrettyPrinter(indent=4)
#     pp.pprint(ranks)


# if __name__ == '__main__':
#     test()