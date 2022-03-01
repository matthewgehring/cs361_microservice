import json
from flask import Flask, request
from wptools import page

def get_meta(title):
    soup = page(title).get_parse()
    infobox = soup.data['infobox']
    return infobox

def get_images(title):
    my_page = page(title).get_parse()
    return my_page.data["image"][0]["url"]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Welcome to my service. POST to /api/data or /api/image to use. Contact Matthew with questions.</h1>"

@app.route('/api/data', methods=['POST'])
def query_records():
    title = request.json
    meta = Flask.jsonify(get_meta(title['title']))
    meta.headers.add('Access-Control-Allow-Origin', '*')
    return meta

@app.route('/api/image', methods=['POST'])
def images():
    title = request.json
    images = get_images(title['title'])
    images = Flask.jsonify(images)
    images.headers.add('Access-Control-Allow-Origin', '*')
    return images

# @app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
# def add_message(uuid):
#     content = request.json
#     print(content['mytext'])
#     return jsonify({"uuid":uuid})

