#!flask/bin/python
from sqlite3 import Timestamp
from flask import Flask, jsonify, abort, make_response, request, redirect
# import http.client, urllib
# import os
# import time
# import requests
import logging
# import json

port = 80

app = Flask(__name__)
app.config["DEBUG"] = True

logging.basicConfig(
	filename='requests.log',
	filemode='w',
	level=logging.DEBUG,
	format='[%(levelname)s] %(message)s'
)

# Adjusting the logger for werkzeug
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.setLevel(logging.DEBUG)

# Adjusting the logger for Flask's app
app.logger.setLevel(logging.DEBUG)

@app.route('/bWAPP/login.php', methods=['POST'])
def login():
    return "/main.php", 302

@app.route('/test', methods=['GET'])
def test():
	logging.info(f'Test Request: {request.path}, Cookies: {request.cookies}')
	return "a2a", 200

@app.route('/bWAPP/login1.php', methods=['POST'])
def login1():
    logging.info(f'Login1 Payload: {request.get_data()}')
    
    # Create a response object to handle cookies
    resp = make_response(redirect('/main.php', code=302))  # Add the redirect URL here
    
    # Set the cookie in the response
    resp.set_cookie(
        'auth_token',
        value='test-token',
        max_age=604800,  # 604800 seconds = 1 week
        secure=True if (request.path).startswith("https") else False,
        httponly=True,
        samesite="Strict",
    )
    
    return resp  # No need to add the status code explicitly, redirect already defaults to 302

@app.route('/bWAPP/login2.php', methods=['POST'])
def login2():
    logging.info(f'Login2 Payload: {request.get_data()}')

    payload = {"result": "success"}
    resp = make_response(jsonify(payload))
    
    # payload = "result=success"
    # resp = make_response(payload, 302)
    
    # resp = make_response(redirect('/main.php', code=302))  # Add the redirect URL here
    
    # Set the cookie in the response
    resp.set_cookie(
        'auth_token',
        value='test-token',
        max_age=604800,  # 604800 seconds = 1 week
        secure=True if (request.path).startswith("https") else False,
        httponly=True,
        samesite="Strict",
    )
    
	# Redirect after setting the payload and cookie
    resp.headers['Location'] = '/main2.php'  # Manually add the redirect URL
    
    return resp, 302  # No need to add the status code explicitly, redirect already defaults to 302

@app.route('/bWAPP/login3.php', methods=['POST'])
def login3():
    logging.info(f'Login3 Payload: {request.get_data()}')
    
    # Create a response object to handle cookies
    resp = make_response(redirect('/main.php', code=302))  # Add the redirect URL here
    
    # Set the cookie in the response
    resp.set_cookie(
        'auth_token',
        value='test-token',
        max_age=604800,  # 604800 seconds = 1 week
        secure=True if (request.path).startswith("https") else False,
        httponly=True,
        samesite="Strict",
    )
    
    return resp  # No need to add the status code explicitly, redirect already defaults to 302

@app.route('/monitors/isalive', methods=['GET'])
def hc():
	return "up", 200

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>')
def catch_all(path):
	return 'You want path: %s' % path

@app.errorhandler(404)
def not_found(error):
	try:
		test_header = request.headers.get('X-Apitest-R')
		logging.info(f' 404 : {request.path} Test: {test_header}')
	except:
		logging.info(f' 404 : {request.path}')
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=port)
	