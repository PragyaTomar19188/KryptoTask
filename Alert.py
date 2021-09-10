import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


alerts = [
    {'alert_id': 0,
     'name': '1',
    },
    {'alert_id': 1,
     'name': '2',},
    {'alert_id': 2,
     'name': '3',}
]

@app.route('/api/v1/create/alert/all', methods=['GET'])
def api_all():
    return jsonify(alerts)

app.run()
@app.route('/api/v1/create/alert', methods=['GET'])
def api_id():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []


    for alert_id in alerts:
        if alert_id['id'] == id:
            results.append(alerts)


    return jsonify(results)

app.run()