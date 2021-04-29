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

@irsystem.route('/', methods=['GET'])
def search():
	# Retrieve values from search query
	query = request.args.get('search')
	difficulty = request.args.get('difficulty')

	require_accessible = request.args.get("requireAccessible")
	require_free_entry = request.args.get("requireFreeEntry")
	require_parking = request.args.get("requireParking")

	walk_on = request.args.get("walkOn")
	hike_on = request.args.get("hikeOn")
	run_on = request.args.get("runOn")
	bike_on = request.args.get("bikeOn")
	horse_on = request.args.get("horseOn")
	swim_on = request.args.get("swimOn")
	ski_on = request.args.get("skiOn")
	snowshoe_on = request.args.get("snowshoeOn")

	distance = request.args.get("setDistance")

	if not query:
		data = []
		output_message = ''
	else:
		# Modify query to include toggle information
		# TODO Change how we process toggles
		if require_accessible:
			query += ' accessible'
		if require_free_entry:
			query += ' free'
		if require_parking:
			query += ' parking'

		# Retrieve rankings in the form of (sim_score, trail_name)
		rankings = get_rankings_by_query(query)
		# Convert rankings into displayable results
		results = [Result(ranking) for ranking in rankings]
		output_message = '🥾 ' + query + ' 🥾'
		data = results

	# Render new outputs
	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)

