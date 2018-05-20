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

def register():
    global access_token
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


def show_whitelists(access_token):
    data = requests.get("{}/{}/whitelists".format(host,api_version), headers={"Authorization":"Bearer {}".format(access_token)}).json()
    print "\nWhitelist Data:"
    print data['Result']['Status']
    print 'IPAddresses', data['IPAddresses']
    print 'GeoLocations', data['GeoLocations']

def show_ip_whitelists(access_token):
    data = requests.get("{}/{}/whitelists/ipaddresses".format(host,api_version), headers={"Authorization":"Bearer {}".format(access_token)}).json()
    print "\nWhitelist Data:"
    print data['Result']['Status']
    print 'IPAddresses', data['IPAddresses']

def search_whitelists(access_token):
    filter = raw_input("Filter: ")
    filter = filter.replace("/", "+")
    data = requests.get("{}/{}/whitelists/ipaddresses/filter/{}".format(host,api_version, filter),
        headers={"Authorization":"Bearer {}".format(access_token)}).json()
    print "Results",data["SearchResult"]["Entries"]

def search_entry_whitelists(access_token):
    filter = raw_input("Entry: ")
    data = requests.get("{}/{}/whitelists/ipaddresses/{}".format(host,api_version, filter),
        headers={"Authorization":"Bearer {}".format(access_token)}).json()
    print "Entry",data["Entry"]

def add_whitelist(access_token):
	ip = raw_input("IP: ")
	comments = ""#raw_input("Comments: ")
	payload = (('IPv4',ip),('Comments',comments))
	data = requests.post("{}/{}/whitelists/create".format(host,api_version), data=payload, headers={"Authorization":"Bearer {}".format(access_token)}).json()
	print	data['Result']['Message']

def show_blacklists(access_token):
    data = requests.get("{}/{}/blacklists".format(host,api_version), headers={"Authorization":"Bearer {}".format(access_token)}).json()
    print "\nBlacklist Data:"
    print data['Result']['Status']
    print 'IPAddresses', data['IPAddresses']
    print 'GeoLocations', data['GeoLocations']

def show_ip_blacklists(access_token):
    data = requests.get("{}/{}/blacklists/ipaddresses".format(host,api_version), headers={"Authorization":"Bearer {}".format(access_token)}).json()
    print "\nBlacklist Data:"
    print data['Result']['Status']
    print 'IPAddresses', data['IPAddresses']

def search_blacklists(access_token):
    filter = raw_input("Filter: ")
    filter = filter.replace("/", "+")
    data = requests.get("{}/{}/blacklists/ipaddresses/filter/{}".format(host,api_version, filter),
        headers={"Authorization":"Bearer {}".format(access_token)}).json()
    print "Results",data["SearchResult"]["Entries"]

def search_entry_blacklists(access_token):
    filter = raw_input("Entry: ")
    data = requests.get("{}/{}/blacklists/ipaddresses/{}".format(host,api_version, filter),
        headers={"Authorization":"Bearer {}".format(access_token)}).json()
    print "Entry",data["Entry"]

def add_blacklist(access_token):
	ip = raw_input("IP: ")
	comments = ""#raw_input("Comments: ")
	payload = (('IPv4',ip),('Comments',comments))
	data = requests.post("{}/{}/blacklists/create".format(host,api_version), data=payload, headers={"Authorization":"Bearer {}".format(access_token)}).json()
	print	data['Result']['Message']



def menu():
    global access_token
    menus = ["Login", "Register", "Show Whitelist", "Show Whitelist IPs",
        "Search Whitelist", "Search Entry Whitelist", "Create Whitelist Entry",
        "Show Blacklist", "Show Blacklist IPs", "Search Blacklist",
        "Search Entry Blacklist", "Create Blacklist Entry"]
    print "\nMenu:\n"
    for i in range(0, len(menus)):
        print i, menus[i]
    print "e Exit"

    opt = raw_input("\nChoose item: ").strip()
    if opt is "e":
        sys.exit()
    if opt is "0":
        login()

    elif opt is "1":
        register()

    elif opt is "2":
        if access_token is "":
            print "Must log in first"
            login()
        show_whitelists(access_token)

    elif opt is "3":
        if access_token is "":
            print "Must log in first"
            login()
        show_ip_whitelists(access_token)

    elif opt is "4":
        if access_token is "":
            print "Must log in first"
            login()
        search_whitelists(access_token)

    elif opt is "5":
        if access_token is "":
            print "Must log in first"
            login()
        search_entry_whitelists(access_token)

    elif opt is "6":
        if access_token is "":
            print "Must log in first"
            login()
        add_whitelist(access_token)

    elif opt is "7":
        if access_token is "":
            print "Must log in first"
            login()
        show_blacklists(access_token)

    elif opt is "8":
        if access_token is "":
            print "Must log in first"
            login()
        show_ip_blacklists(access_token)

    elif opt is "9":
        if access_token is "":
            print "Must log in first"
            login()
        search_blacklists(access_token)

    elif opt is "10":
        if access_token is "":
            print "Must log in first"
            login()
        search_entry_blacklists(access_token)

    elif opt is "11":
        if access_token is "":
            print "Must log in first"
            login()
        add_blacklist(access_token)

while True:
    menu()
