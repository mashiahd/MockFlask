
	# return jsonify({"id": "555"})
	# cookie = set_cookie()
	# return "", 200

# @app.route('/close-test/alerts.json', methods=['GET'])
# def close_test():
#         logging.info(f'Redalert Request - Ganei Tikva')
#         return jsonify({"id": "555", "data": ['סביון']})

# @app.route('/merkaz-test/alerts.json', methods=['GET'])
# def merkaz_test():
#         logging.info(f'Redalert Request - Ganei Tikva')
#         # return jsonify({"id": "555", "data": ['הרצליה']})
#         return "", 200
# @app.route('/north-test/alerts.json', methods=['GET'])
# def north_test():
#         logging.info(f'Redalert Request - Ganei Tikva')
#         return jsonify({"id": "555", "data": ['עתלית']})

# @app.route('/users/v1/login', methods=['POST'])
# def bruteforce():
#       data = request.get_json()
#       if data is not None:
#               user = data.get('username')
#               password = data.get('password')  # Ensure you're using the correct key here, not 'passowrd'
#               logging.info(f'User: {user} /// Pass: {password}')
#               if user == 'vagrant' and password == 'monkey':
#                       return jsonify("BruteForce Succeed")
#               else:
#                       return "Tried but failed"
#       else:
#               return "Invalid JSON", 400

# @app.route('/users/v1/login', methods=['POST'])
# def bruteforce():
#       data = request.get_json()
#       if data is not None:
#               user = data.get('username')
#               password = data.get('password')  # Ensure you're using the correct key here, not 'passowrd'
#               logging.info(f'Login User: {user} & Pass: {password}')
#               return jsonify({"status": "success", "auth_token": "1q2w3e4r5t6y7u"})

# @app.route('/users/v1/register', methods=['POST'])
# def register():
#       data = request.get_json()
#       if data is not None:
#               username = data.get('username')
#               password = data.get('password')
#               email = data.get('email')
#               logging.info(f'User Register - Username: {username}, Email: {email}')

#               return jsonify({"status": "success"})

# @app.route('/xff_attack', methods=['GET'])
# def xff_attack():
	# source_ip = request.remote_addr
	# headers_to_log = [
	#         "Client-IP",
	#         "X-Real-Ip",
	#         "Redirect",
	#         "Referer",
	#         "X-Client-IP",
	#         "X-Custom-IP-Authorization",
	#         "X-Forwarded-By",
	#         "X-Forwarded-For",
	#         "X-Forwarded-Host",
	#         "X-Forwarded-Port",
	#         "X-True-IP",
	#         "X-Zm-True-IP",
	#         "X-Zm-Client-IP"
	#         ]

	# for header in headers_to_log:
	#         header_value = request.headers.get(header)
	#         if header_value:
	#                 logging.info(f'{header} from IP {source_ip}: {header_value}')
	#         else:
	#                 logging.info(f'{header} header not present in request from IP {source_ip}')

	# return "OK"

# @app.route('/pve/shutdown/<string:pve>', methods=['POST'])
# def poweroff(pve):
#         selected_pve = request.headers.get(pve)
#         proxmox = ProxmoxAPI(
#         "192.168.15.150",
#         user="admin@pam",
#         password="secret_word",
#         verify_ssl=False
# )

# @app.route('/api/get-country-extras/<string:country_code>', methods=['GET'])
# def cc(country_code):
#       pwd = "/api/get-country-extras/"
#       attack_header = request.headers.get("X-AttackB0t")
#       logging.info(f' Log: {pwd}{country_code} - Attack Header: {attack_header}')
#       return "OK"

# @app.route('/api/v2/tareweight/get/<int:get_id>', methods=['GET'])
# def get_id(get_id):
#       pwd = "/api/v2/tareweight/get/"
#       logging.info(f' Log: {pwd}{get_id}')
#       return "OK"

# @app.route('/api/v2/tariffcalculator/getmarineports/<int:getmarineports_id>', methods=['GET'])
# def getmarineports_id(getmarineports_id):
#       pwd = "/api/v2/tariffcalculator/getmarineports/"
#       logging.info(f' Log: {pwd}{getmarineports_id}')
#       return "OK"

# @app.route('/api/v2/storagecertificate/getpdf/<string:getpdf_id>', methods=['GET'])
# def getpdf_id(getpdf_id):
#       pwd = "/api/v2/storagecertificate/getpdf/"
#       source_ip = request.remote_addr
#       headers_to_log = [
#               "Client-IP",
#               "X-Real-Ip",
#               "Redirect",
#               "Referer",
#               "X-Client-IP",
#               "X-Custom-IP-Authorization",
#               "X-Forwarded-By",
#               "X-Forwarded-For",
#               "X-Forwarded-Host",
#               "X-Forwarded-Port",
#               "X-True-IP",
#               "X-Zm-True-IP",
#               "X-Zm-Client-IP"
#               ]

#       for header in headers_to_log:
#               header_value = request.headers.get(header)
#               if header_value:
#                       logging.info(f' {header}: {header_value} from SRC_IP: {source_ip}: ')
#               # else:
#                       # all_headers = dict(request.headers)
#                       # logging.info(f' All headers: {all_headers}')
#                       # logging.info(f' Log: {pwd}{getpdf_id}')
#       return "OK"