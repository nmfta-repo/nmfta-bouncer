import requests, sys
if len(sys.argv) < 2:
    exit()

api_version = "v1"
host = sys.argv[1]
access_token = ""

menus = ["Login", "Register", "Whitelist"]

for i in range(0, len(menus)):
    print i, menus[i]

opt = raw_input("\nChoose item: ").strip()

if opt is "0":
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    payload = (('username', username), ('password', password), ('grant_type', 'password'))
    data = requests.post("{}/{}/login".format(host,api_version), data=payload).json()
    if 'access_token' in data:
        access_token = data['access_token']
        print "good login"
    else:
        print "login failed:", data['message']

elif opt is "1":
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    payload = (('username', username), ('password', password))
    data = requests.post("{}/{}/register".format(host,api_version), data=payload).json()
    print data
