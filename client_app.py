import requests, sys

api_version = "v1"
host =  "http://localhost:8080" if len(sys.argv) < 2 else sys.argv[1]
access_token = ""

def login():
    global access_token
    username = "icon"#raw_input("Username: ")
    password = "test"#raw_input("Password: ")
    payload = (('username', username), ('password', password), ('grant_type', 'password'))
    data = requests.post("{}/{}/login".format(host,api_version), data=payload).json()
    if 'access_token' in data:
        access_token = data['access_token']
        print "good login"
    else:
        print "login failed:", data['message']


if __name__ == "__main__":
    login()
    opt = raw_input("\n\n1) Whitelist\n2) Blacklist\n\nOpt: ")
    ltype = "bl"
    if "1" in opt:
        ltype = "wl"
    opt = raw_input("""\n\n1) View All\n2) View IPs\n3) Show Entry
            4) Search Entry\n5) Update Entry\n6) Manual\n:""")
    if "6" in opt:
        opts = raw_input("\nEnter: ")
        data = requests.get("{}/{}/{}".format(host,api_version, opts), headers={"Authorization":"Bearer {}".format(access_token)}).json()
