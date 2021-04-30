from app.irsystem.models.inverted_index import InvertedIndex
from app.irsystem.models.get_data import idx_to_trail_name

inv_idx_accessibility = InvertedIndex(token_type='attributes', vector_type='binary').inv_idx['Wheelchair friendly']

def get_accessibility_ranking(accessibility_required):
    rankings = {}
    if accessibility_required:
        for i in inv_idx_accessibility:
            rankings[idx_to_trail_name[i]] = 1
    return rankings