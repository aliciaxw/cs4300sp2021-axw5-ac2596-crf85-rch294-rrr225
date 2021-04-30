def get_filter_score(query, trail):
    """
    Given a boolean value for accessibility in query and accessibility in trail, return
    1 if (query, trail) == (1,1) or (query, trail) == (0,0).
    """
    return 1 if (query == 0 and trail == 0) or (query == 1 and trail == 1) else 0

def get_filter_scores(query):
    """
    Given a query, returns a dictionary of trail_name to accessibility filter scores.
    """
    pass