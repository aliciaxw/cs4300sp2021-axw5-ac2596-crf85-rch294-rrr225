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
# weights for adjusting ranking weights
alpha = 0.1
beta = 0.05

# Mapping of trail_id to result object after query
global_results = {}

@irsystem.route('/', methods=['GET', 'POST'])
def search():
	global global_results
	global global_weights

	if "good" in request.args:
		update_weights_rocchio(True, global_results[int(request.args['good'])])
		output_message = f"👍 Your opinion has been received! 👍"
		return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=global_results.values())
	elif "bad" in request.args:
		update_weights_rocchio(False, global_results[int(request.args['bad'])])
		output_message = f"👎 Your opinion has been received! 👎"
		return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=global_results.values())
	else:
		# Retrieve values from search query
		query = request.args.to_dict()

		if query == empty_query or query == {}:
			data = []
			output_message = ''
		else:
			# Retrieve rankings in the form of (sim_score, trail_name)
			results = get_rankings_by_query(query, global_weights)
			# Add results to global results for rocchio update
			global_results = { result.id:result for result in results}
			output_message = f"🥾 your query: {query['search']} 🥾"
			data = results

		# Render new outputs
		return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)

def update_weights_rocchio(isRelevant, result):
	"""
	Will update ranking result weights based on relevance feedback from user.
	"""
	global global_weights
	max_contributing_weight = max(result.sim_measures, key=result.sim_measures.get)
	if isRelevant:
		global_weights[max_contributing_weight] += alpha
		for measure in result.sim_measures:
			global_weights[measure] -= beta 

	else:
		global_weights[max_contributing_weight] -= alpha
		for measure in result.sim_measures:
			global_weights[measure] += beta 