from collections import Counter
import numpy as np
from nltk.tokenize import TreebankWordTokenizer
from app.irsystem.models.inverted_index import InvertedIndex
from app.irsystem.models.get_data import idx_to_trail_name, NUM_DOCS
import math

def get_rankings_by_query(query, alpha=0.7, beta=0.3):
    """
    Returns a list of the top 3 rankings in the form (similarity_score, trail_name) given a query string.
    This serves as the main function that is called when a new query is made.
    """
    sim_descriptions = get_cosine_similarity_ranking(query, 'descriptions')
    sim_reviews = get_cosine_similarity_ranking(query, 'reviews')
    
    # assert len(sim_descriptions) == len(sim_reviews)s
    
    # 70 description and 30 reviews
    final_sim = {}
    for name in sim_descriptions:
        final_sim[name] = alpha * sim_descriptions[name] + beta * sim_reviews[name]
    
    rankings = [(final_sim[name], name) for name in final_sim]
    rankings.sort(key = lambda x: (-x[0],x[1]))
    rankings = rankings[:3]
    print(rankings)
    return rankings
        
        

def get_cosine_similarity_ranking(query, token_type):
    # Create tfidf matrix object for trail documents with 200 features
    trails_tfidf_obj = InvertedIndex(token_type=token_type, vector_type='tf')
    inv_idx = trails_tfidf_obj.inv_idx
    idfs= trails_tfidf_obj.idfs
    doc_norms = trails_tfidf_obj.doc_norms
    # Create tfidf vector for query of size (1, 200)
    q_tfs = Counter(tokenize_string(query))
    q_norm = math.sqrt(sum([(q_tfs[tok] * idfs[tok])**2 for tok in q_tfs if tok in idfs]))
    
    nums = {}
    for tok in q_tfs:
        if tok in idfs:
            tf_idf_q = q_tfs[tok] * idfs[tok]
            for post in inv_idx[tok]:
                val = nums.get(post[0], 0)
                val += tf_idf_q * (post[1] * idfs[tok])
                nums[post[0]] = val

    # rankings = [(nums[i]/(q_norm * doc_norms[i]), i) for i in nums]
    # rankings.sort(key = lambda x: (-x[0],x[1]))
    # rankings = [(rank[0], idx_to_trail_name[rank[1]])for rank in rankings]

    ans = {}
    for i in nums:
        ans[idx_to_trail_name[i]] = nums[i]/(q_norm * doc_norms[i])
    return ans

def tokenize_string(s):
    """
    Given an input string s, returns a list of tokens in the string.
    """
    tokenize = TreebankWordTokenizer().tokenize
    return tokenize(s.lower())


def tfidfize_query(q, features, idfs):
    """
    Given an input list of tokens q, returns a tfidf vector of size (1, [# of features]) representing q.
    If a term appears in q that is not in the given features, ignore it.
    """
    tfidf_vec = np.zeros(len(features))
    tf_q = { term:freq for term, freq in Counter(q).items() if term in idfs }

    for i, token in enumerate(features):
        tfidf_vec[i] = tf_q.get(token, 0) * idfs.get(token, 0)

    return tfidf_vec


def cosine_sim(query, trail):
    """
    Returns cosine similarity of query and a trail document.
    """
    num = np.dot(query, trail)
    denom = (np.sqrt(np.sum(np.linalg.norm(query))) * np.sqrt(np.sum(np.linalg.norm(trail))))
                 
    return num / denom
 

def cosine_sim_matrix(num_trails, query, tfidf, sim_method = cosine_sim):
    # trails_sims = np.zeros(num_trails)
    trails_sims = [0 for _ in range(num_trails)]
 
    # for each trail document find the cosine similarity with the query
    for i in range(0, num_trails):
        trails_sims[i] = (sim_method(query, tfidf[i]), idx_to_trail_name[i])
    
    # sorted list of all cosine similarity scores of query and trail documents
    ranked_trails = sorted(trails_sims, key= lambda x: -x[0])
    return ranked_trails


def get_filter_score(query, trail):
    """
    Given a boolean value for accessibility in query and accessibility in trail, return
    1 if (query, trail) == (1,1) or (query, trail) == (0,0).
    """
    return 1 if (query == 0 and trail == 0) or (query == 1 and trail == 1) else 0

