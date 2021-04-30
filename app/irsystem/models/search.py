from collections import Counter
from app.irsystem.models.cosine import get_cosine_similarity_ranking
from app.irsystem.models.get_data import data
from app.irsystem.models.get_data import trail_names
from app.irsystem.models.jaccard import get_jaccard_scores
from app.irsystem.models.levenshtein import ranked_levs
from app.irsystem.models.l2distance import get_l2_distance
from app.irsystem.models.accessibility import get_accessibility_ranking
import math


def get_rankings_by_query(query, a=0.5, b=0.3, c=0.2, d=0.1, e=0.2):
    """
    Returns a list of the top 3 rankings in the form (similarity_score, trail_name) given a query string.
    This serves as the main function that is called when a new query is made.

    a -> weight for descriptions similarity
    b -> weight for reviews similarity
    c -> weight for title similarity
    """
    # {'search': 'Easy hiking trail', 'difficulty': 'easy', 'requireAccessible': 'on',
    # 'requireFreeEntry': 'on', 'requireBathroom': 'on', 'walkOn': 'on', 'hikeOn': 'on',
    # 'runOn': 'on', 'bikeOn': 'on', 'horseOn': 'on', 'swimOn': 'on', 'skiOn': 'on',
    # 'snowshoeOn': 'on', 'setDistance': '5'}
    sim_descriptions = get_cosine_similarity_ranking(
        query['search'], 'descriptions')
    sim_reviews = get_cosine_similarity_ranking(query['search'], 'reviews')
    sim_titles = ranked_levs(query['search'], trail_names)
    sim_distance = get_l2_distance(query['setDistance'])
    sim_accessibility = get_accessibility_ranking('requireAccessible' in query)

    sim_jaccard = get_jaccard_scores(query, data)

    # TODO
    # strict filter scores for accessibility

    final_sim = {}
    for name in trail_names:
        final_sim[name] = 1 * (
            a * sim_descriptions.get(name, 0) +
            b * sim_reviews.get(name, 0) +
            c * sim_titles.get(name, 0) +
            d * sim_distance.get(name, 0) +
            e * sim_jaccard.get(name, 0))

    rankings = [(final_sim[name], name) for name in final_sim]
    rankings.sort(key=lambda x: (-x[0], x[1]))
    print(rankings)

    rankings = rankings[:3]

    return rankings
