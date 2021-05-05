from app.irsystem.models.get_data import data, trail_to_idx
import random


class Result:
    """
    Contains all the data needed to display a query result. 
    Takes in a tuple of (Cosine Similarity Score, Trail Name).

    Attributes include:
        - trail name (string)
        - GPS coordinates (float list)
        - difficulty (string)
        - activity types (dict)
        - attributes (list)
        - description (string)
        - reviews (tuple list)
        - random review (string)
    """

    def __init__(self, sim_tup, **kwargs):
        self.name = sim_tup[1]
        ith_trails = data[self.name]

        self.gps = ith_trails['GPS']
        self.length = ith_trails['Distance']
        self.difficulty = ith_trails['Difficulty']
        self.attributes = []
        # activities = ["Walking", "Hiking", "Running", "Biking", "Horseback Riding", "Cross-Country Skiiing", "Snowshoeing"]
        activities = {"Walking": "static/walk-active.svg", "Hiking": "static/hike-active.svg", "Running": "static/run-active.svg", "Biking": "static/bike-active.svg",
                      "Horseback Riding": "static/horse-active.svg", "Cross-Country Skiiing": "static/ski-active.svg", "Snowshoeing": "static/snowshoe-active.svg"}
        # self.activity_types = { i : False for i in activities }
        self.activity_types = []
        for attribute in ith_trails['Trail Attributes']:
            if attribute[9:] in activities:
                self.activity_types.append(activities[attribute[9:]])
            else:
                self.attributes.append(attribute)
        self.attributes = self.attributes[:3]
        self.description = ith_trails['Description']
        self.reviews = []
        for review in ith_trails["Reviews"]:
            if review['comment'] != "" and review['rating'] != None:
                self.reviews.append((review["comment"], review["rating"]))
                # self.reviews.append(review)
        # self.review = self.reviews[random.randint(0, len(self.reviews)-1)]
        self.review = self.getReviews(self.reviews)
        self.img = ith_trails['image id']
        print(self.img)
        self.url = "https://ithacatrails.org/trail/" + str(ith_trails["Ithacatrails ID"])
        # similarities corresponding to weights
        self.sim_measures = {
            "a": sim_tup[0]['a'],
            "b": sim_tup[0]['b'],
            "c": sim_tup[0]['c'],
            "d": sim_tup[0]['d'],
            "e": sim_tup[0]['e']
        }
        # self.accessibility_types = kwargs.get('accessibility_types')

    def getReviews(self, reviews):
        """
        Returns a dicitonary: 
            { 'good' : [good_review], 'bad' : [bad_review] }

        where [good_review] is a review with a positive sentiment, and a 
        [bad_review] is a review with a negative sentiment.

        A good review should have a high
        """
        # print(reviews)

        sorted_reviews = sorted(
            reviews, key=lambda tup: (tup[1], -len(tup[0])))
        return {
            'good': sorted_reviews[len(sorted_reviews) - 1],
            'bad': sorted_reviews[0]
        }
        # return sorted_reviews


# Test Code
# ---------
# rslt = Result((.25, "Ellis Hollow Yellow trail"))
# print(rslt.name)
# print(rslt.difficulty)
# print(rslt.gps)
# print(rslt.length)
# print(rslt.description)
# print(rslt.activity_types)
# print(rslt.reviews)
# print(rslt.attributes)
# print(rslt.activity_types)
