from flask import Flask
from flask_restful import Api
import os
import json

curr_path = os.path.dirname(os.path.abspath(__file__))

with open(curr_path+"/config/config.json") as f:
	config = json.load(f)

try:
	with open(curr_path+"/config/dev_config.json") as f:
		dev_config = json.load(f)
except Exception as e:
	dev_config = {}

app = Flask(__name__)
api = Api(app)

host = config["host"]
port = config["port"]
debug = dev_config["debug"] if ("debug" in dev_config) else False

# Import Services

import services.home.home
import services.test.test

if __name__ == '__main__':
	app.run(host=host, port=port, debug=debug)