import requests, sys

api_version = "v2"
host =  "http://localhost:8080" if len(sys.argv) < 2 else sys.argv[1]
access_token = ""

username = "icon"#raw_input("Username: ")
password = "test"#raw_input("Password: ")
payload = (('username', username), ('password', password))
data = requests.post("{}/{}/register".format(host,api_version), data=payload).json()
print data['message']
payload = (('username', username), ('password', password), ('grant_type', 'password'))
data = requests.post("{}/{}/login".format(host,api_version), data=payload).json()
if 'access_token' in data:
    access_token = data['access_token']
    print "good login"
else:
    print "login failed:", data['message']
