# from __main__ import app
from __main__ import api, config, dev_config, debug
from flask_restful import Resource
from flask import request
import json


class test(Resource):

	def get(self):

		try:
			
			ret_obj = {
				"status" : "success",
				"success" : True,
				"data" : {
					"test" : "Test Successful"
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


class hello(Resource):

	def get(self):

		try:

			ret_obj = {
				"status" : "success",
				"success" : True,
				"data" : {
					"hello" : "Hello Bro"
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

	def post(self):

		try:

			try:
				input_data = request.json
			except Exception as e:
				ret_obj = {
					"status" : "failure",
					"success" : False,
					"error" : {
						"id" : "",
						"message" : "Post Data Not Found / Not in JSON format"
					}
				}
				ret_status = 400

				return ret_obj, ret_status


			ret_obj = {
				"status" : "success",
				"success" : True,
				"data" : {
					"hello" : {
						"input_data" : input_data
					}
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



class hello_name(Resource):

	def get(self, name):

		try:

			ret_obj = {
				"status" : "success",
				"success" : True,
				"data" : {
					"hello" : "Hello "+name
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



api.add_resource(test, '/test', resource_class_kwargs={})
api.add_resource(hello, '/hello', resource_class_kwargs={})
api.add_resource(hello_name, '/hello/<string:name>', resource_class_kwargs={})