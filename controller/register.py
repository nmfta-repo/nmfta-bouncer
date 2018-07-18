import requests, sys

api_version = "v2"
access_token = ""

host = ""
if len(sys.argv) > 1:
    server = sys.argv[1]
    port = sys.argv[2]
    host = "http://{}:{}".format(server, port)

username = "icon"#raw_input("Username: ")
password = "test"#raw_input("Password: ")
payload = (('username', username), ('password', password))
data = requests.post("{}/{}/register".format(host,api_version), data=payload).json()
print(data['message'])
