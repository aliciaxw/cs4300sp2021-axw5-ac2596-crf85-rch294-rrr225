from . import *  
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder
from app.irsystem.models.search import *
from app.irsystem.models.result import Result

project_name = "Hiking Trail Recommender"
net_id = "Ryan Richardson (rrr225) " + \
		 "Alicia Wang (axw5) " + \
		 "Alicia Chen (ac2596) " + \
		 "Cesar Ferreyra-Mansilla (crf85) " + \
		 "Renee Hoh (rch294)"
empty_query = {'search': ''}

# weights to be updated
a = 0.5
b = 0.3
c = 0.2
d = 0.1
e = 0.2

@irsystem.route('/', methods=['GET'])
def search():
	# Retrieve values from search query
	query = request.args.to_dict()

	if query == empty_query or query == {}:
		data = []
		output_message = ''
	else:
		# Retrieve rankings in the form of (sim_score, trail_name)
		results = get_rankings_by_query(query, a, b, c, d, e)
		output_message = f"🥾 your query: {query['search']} 🥾"
		data = results

	# Render new outputs
	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)

