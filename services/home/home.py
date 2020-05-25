# from __main__ import app
from __main__ import api, config, dev_config, debug
from flask_restful import Resource
from flask import request
import json


class home(Resource):

	def get(self):

		try:
			
			ret_obj = {
				"status" : "success",
				"success" : True,
				"data" : {
					"test" : "Heyyy.. Welcome"
				}
			}
			ret_status = 200

			return ret_obj, ret_status

		except Exception as e:

			ret_obj = {
				"status" : "failure",
				"success" : False,
				"error" : {
					"id" : "",
					"message" : str(e)
				}
			}
			ret_status = 500

			return ret_obj, ret_status

api.add_resource(home, '/', resource_class_kwargs={})
