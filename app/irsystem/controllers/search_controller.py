from . import *
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder
from app.irsystem.models.search import *

project_name = "Hiking Trail Recommender"
net_id = "Ryan Richardson (rrr225) " + \
    "Alicia Wang (axw5) " + \
    "Alicia Chen (ac2596) " + \
    "Cesar Ferreyra-Mansilla (crf85) " + \
    "Renee Hoh (rch294)"
empty_query = {'search': ''}

# weights to be updated
global_weights = {
	"a": 0.5,
	"b": 0.3,
	"c": 0.2,
	"d": 0.1,
	"e": 0.2
}


@irsystem.route('/', methods=['GET'])
def search():
	# Retrieve values from search query
	query = request.args.to_dict()

	if query == empty_query or query == {}:
		data = []
		output_message = ''
	else:
		# Retrieve rankings in the form of (sim_score, trail_name)
		results = get_rankings_by_query(query, global_weights)
		output_message = f"🥾 your query: {query['search']} 🥾"
		data = results

	# Render new outputs
	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data, query=query)

# @irsystem.route('/', methods=['POST'])
# def update_weights_rocchio(isRelevant, result):
# 	"""
# 	Will update ranking result weights based on relevance feedback from user.
# 	"""
# 	max_contributing_weight = max(result.sim_measures, key=result.sim_measures.get)

# 	if request.form['feedback'] == 'good':
# 		global_weights[max_contributing_weight] += 0.1
# 	elif request.form['feedback'] == 'bad':
# 		global_weights[max_contributing_weight] -= 0.1
