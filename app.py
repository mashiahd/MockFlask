#!flask/bin/python
from sqlite3 import Timestamp
from flask import Flask, jsonify, abort, make_response, request, redirect
import logging
import time

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

# @app.before_request
# def decode_latin1():
# 	if request.data:
# 		request._cached_data = request.data.decode('latin-1')
# 	if request.form:
# 		request._cached_form = {k: v for k, v in request.form.items()}
# 	if request.query_string:
# 		request._cached_query_string = request.query_string.decode('latin-1')


@app.route('/bWAPP/login.php', methods=['POST'])
def login():
	logging.info(f'Login Payload: {request.get_data()}')
	# Create a response object to handle cookies
	resp = make_response(redirect('/main.php', code=302))  # Add the redirect URL here
	
	# Set the cookies in the response
	resp.set_cookie(
		'PHPSESSID',
		value='8a1b5aeda7232ec9f7abfa9539f15f10',
		path='/',
		max_age=604800  # 604800 seconds = 1 week
	)
	resp.set_cookie(
		'security_level',
		value='0',
		expires='Thu, 01-Jan-2026 12:16:43 GMT',
		path='/',
		max_age=604800  # 604800 seconds = 1 week
	)
	
	print("Login Was Made")
	return resp  # No need to add the status code explicitly, redirect already defaults to 302

@app.route('/test', methods=['GET'])
def test():
	logging.info(f'Test Request: {request.path}, Cookies: {request.cookies}')
	return "a2a", 200

@app.route('/bWAPP/login.php', methods=['POST'])
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

@app.route('/bWAPP/sqli_1.php', methods=['GET'])
def sqli_1():
	print(f"Path Accessed: {request.path}")
	print(f"Query String: {request.query_string}")
	return "sqli_1", 200

@app.route('/bWAPP/sqli_13.php', methods=['POST'])
def sqli_13():
	print(f"Path Accessed: {request.path}")
	print(f"Query String: {request.query_string}")
	return "sqli_13", 200

@app.route('/bWAPP/sqli_7.php', methods=['POST'])
def php():
	print(f"Path Accessed: {request.path}")
	print(f"Body: {request.get_data()}")
	return "sqli_7", 200

@app.route('/bWAPP/sqli_user_agent.php', methods=['GET'])
def sqli_user_agent():
	print(f"Path Accessed: {request.path}")
	print(f"Header (UA): {request.headers.get('User-Agent')}")
	return "sqli_user_agent", 200

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
def catch_all(path):
	if request.method == 'POST':
		data = request.form if request.form else request.get_json()
		print(f'Catch POST: {path}?{request.query_string}, Data: {data}')
	else:
		print(f'Catch: {path}?{request.query_string}')
	# time.sleep(120)  # Simulate a timeout by sleeping for 60 seconds
	# return '', 408 .ץ.ץ.ץ.ץ  # Return a 408 Request Timeout status
	return '', 200

@app.errorhandler(404)
def not_found(error):
	try:
		test_header = request.headers.get('X-Apitest-R')
		logging.info(f' 404 : {request.path} Test: {test_header}')
	except:
		logging.info(f' 404 : {request.path}')
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=port)
