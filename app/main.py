from flask import Flask, request, jsonify
from wptools import page

def get_meta(title):
    soup = page(title).get_parse()
    infobox = soup.data['infobox']
    return infobox

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Welcome to my service. POST to /api to use. Contact Matthew with quesitons.</h1>"

@app.route('/api', methods=['POST'])
def query_records():
    title = request.json
    meta = get_meta(title['title'])
    return jsonify(meta)

# @app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
# def add_message(uuid):
#     content = request.json
#     print(content['mytext'])
#     return jsonify({"uuid":uuid})

