from flask import Flask, request, jsonify
from tools import get_meta

app = Flask(__name__)

@app.route('/', methods=['POST'])
def query_records():
    title = request.json
    meta = get_meta(title['title'])
    return jsonify(meta)

# @app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
# def add_message(uuid):
#     content = request.json
#     print(content['mytext'])
#     return jsonify({"uuid":uuid})

app.run(debug=True)