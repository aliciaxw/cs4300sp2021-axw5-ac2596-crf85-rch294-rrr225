from collections import Counter
from app.irsystem.models.cosine import get_cosine_similarity_ranking
from app.irsystem.models.get_data import trail_names
from app.irsystem.models.levenshtein import ranked_levs
import math

def get_rankings_by_query(query, a=0.5, b=0.3, c=0.2):
    """
    Returns a list of the top 3 rankings in the form (similarity_score, trail_name) given a query string.
    This serves as the main function that is called when a new query is made.

    a -> weight for descriptions similarity
    b -> weight for reviews similarity
    c -> weight for title similarity
    """
    sim_descriptions = get_cosine_similarity_ranking(query, 'descriptions')
    sim_reviews = get_cosine_similarity_ranking(query, 'reviews')
    sim_titles = ranked_levs(query, trail_names)

    # TODO
    # strict filter scores
    # jaccard scores

    final_sim = {}
    for name in trail_names:
        final_sim[name] = a * sim_descriptions.get(name, 0) + \
        b * sim_reviews.get(name, 0) + \
        c * sim_titles.get(name, 0)
    
    rankings = [(final_sim[name], name) for name in final_sim]
    rankings.sort(key = lambda x: (-x[0],x[1]))
    rankings = rankings[:3]

    print(rankings)
    return rankings