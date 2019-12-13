#import secrets
import random
import string
import base64

import json
import names

debug_ = True
br = False


headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'dashboard.vimoearn.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}



def register_http(user_refrence_code=""):
	#id_ = secrets.token_hex(16)
	
	id_ = str('%030x' % random.randrange(16**30))[-10:]
	post_data_ = {"sign":"9f078cb0ebc3c5bf5f9b775727a7989e","key":"167","method_name":"user_register","name": "","email":"","password":"password12345","device_id":"","phone":"9732202402","user_refrence_code":""}
	post_data_["name"] = names.get_full_name()
	post_data_["email"] = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@ymail4.com"
	post_data_["device_id"] = "3a49b1b" + id_
	post_data_["user_refrence_code"] = user_refrence_code
	n_ = "9"
	for b in range(9): n_ = n_ + random.SystemRandom.choices(random,"1234567890")[0]
	post_data_["phone"] = n_
	post_data_ = str(post_data_).replace("\'", "\"")
	#print(post_data_)
	post_data_ = (base64.b64encode(str(post_data_).encode()).decode()[:-1])
	#
	#print(post_data_)
	if br:
		r_ = requests.post("https://dashboard.vimoearn.com/api_new.php", data={"data" : post_data_}, headers=headers)
		#r_ = r_.text
	else:
		curl = pycurl.Curl()
		curl.setopt(pycurl.URL, 'https://dashboard.vimoearn.com/api_new.php')
		curl.setopt(pycurl.POST, 1)
		body_as_dict  = {"data" : post_data_}
		body_as_json_string = json.dumps(body_as_dict) # dict to json
		body_as_file_object = StringIO(body_as_json_string)
		curl.setopt(pycurl.READDATA, body_as_file_object) 
		curl.setopt(pycurl.POSTFIELDSIZE, len(body_as_json_string))
		curl.perform()
		curl.close()
	return(r_)


#print(''.join(random.choices(string.ascii_lowercase + string.digits, k=6)))
def __main__():
	print("[=] A Script by Bugl3ss C0d3r [=] \n")
	print("[=] Feel free to contact me on tg @bugl3ssC0d3r [=] \n\n")

	promo_code = "qydc6vxz"
	i = 900
	while (1):
		_ = register_http(promo_code)
		if debug_: print(str(_))
		print("[#] Referral Number: " + str(i) + " ;) Haha!!"); i = i + 1
	print( str(n) + "[#] Referrals Added Successfully!")
	

if __name__ == "__main__":
	try:
		import pycurl
		from cStringIO import StringIO
	except ImportError:
		if debug_: print( "[!] " + "faster-than-requests module not found. Using default requests module. \n")
		try:
			import requests
			br = True
		except:
			if debug_: print( "[!] " + "Please install the requests module!" + '\n')
			if debug_: print( "[!] " + "pip3 install requests")
	# Run Main
	__main__()
