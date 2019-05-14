import datetime
from dateutil.relativedelta import relativedelta
from bouncerapi.bouncerapi_client import BouncerapiClient
from bouncerapi.configuration import Configuration
from bouncerapi.exceptions.api_exception import APIException
from bouncerapi.models import register_new_user_request, login_to_bouncer_api_request, login_to_bouncer_api_response, ip_address

#set the Bouncer REST API location
Configuration.default_host = "localhost:8080"
TEST_USER = "testpython"
TEST_USER_PASSWORD = "python#2019"

def registerNewUser():
    """ Register New User

    """
    # NOTE: To Call this method, the Bouncer Rest API interface should have been started with the --testing parameter
    client = BouncerapiClient()
    try:
        register_request = register_new_user_request.RegisterNewUserRequest(username=TEST_USER, password=TEST_USER_PASSWORD)
        register_response = client.users_login_registration.register_new_user(register_request)
    except APIException as exception:
        if exception.response_code == 403:
            print("Unable to register user")

def getBouncerApiSdkClient():
    """ Helper method that automatically authenticates with the bouncer API and returns the SDK client

    """
    client = BouncerapiClient()
    if (Configuration.ACCESS_TOKEN == None):
        loginRequest = login_to_bouncer_api_request.LoginToBouncerAPIRequest(username=TEST_USER, 
        password=TEST_USER_PASSWORD, grant_type="password")
        response = client.users_login_registration.login_to_bouncer_api(body=loginRequest)
        Configuration.ACCESS_TOKEN = response.access_token
    return client

def addWhiteList(new_ipAddress):
    """ Adds a whitelist entry to the appliance firewall using the REST API

    Args:
            new_ipAddress (string): A valid string representation of IP Address.

    """
    client = getBouncerApiSdkClient()
    try:
        whitelist_address = ip_address.IPAddress(start_date=datetime.datetime.now(), end_date=datetime.datetime.now() + relativedelta(years=1), active=True, i_pv_4=new_ipAddress)
        whitelist_address.comments = "Adding IP Address"
        response = client.whitelist_ip_addresses.create(whitelist_address)
        print("{} added to whitelist successfully".format(new_ipAddress))
    except APIException as exception:
        print("unable to add whitelist entry")

def addBlackList(new_ipAddress):
    """ Adds a blacklist entry to the appliance firewall using the REST API

        Args:
            new_ipAddress (string): A valid string representation of IP Address.

    """
    client = getBouncerApiSdkClient()
    try:
        blacklist_address = ip_address.IPAddress(start_date=datetime.datetime.now(), end_date=datetime.datetime.now() + relativedelta(years=1), active=True, i_pv_4=new_ipAddress)
        blacklist_address.comments = "Adding IP Address"
        response = client.blacklist_ip_addresses.create(blacklist_address)
        print("{} added to blacklist successfully".format(response.result.entry_id))
        return response
    except APIException as exception:
        print("unable to add blacklist entry")
        if (exception.context != None and exception.context.response.raw_body != None):
            print(exception.context.response.raw_body)

def removeBlackList(response,new_ipAddress):
    """ Removes a blacklist entry from the appliance firewall using the REST API

        Args:
            new_ipAddress (string): A valid string representation of IP Address.

    """
    client = getBouncerApiSdkClient()
    try:
        blacklist_address = ip_address.IPAddress(start_date=datetime.datetime.now(), end_date=datetime.datetime.now() + relativedelta(years=1), active=True, i_pv_4=new_ipAddress)
        removeResponse = client.blacklist_ip_addresses.remove(response.result.entry_id, body = blacklist_address)
        print("{} {}".format(new_ipAddress, removeResponse.result.message))
        return removeResponse
    except APIException as exception:
        print("unable to remove blacklist entries")
        if (exception.context != None and exception.context.response.raw_body != None):
            print(exception.context.response.raw_body)

def listWhiteList():
    """ Retrieves the current whitelisted entries from the appliance firewall using the REST API

    """
    client = getBouncerApiSdkClient()
    try:
        response = client.whitelist_ip_addresses.list()
        return response
    except APIException as exception:
        print("unable to list whitelist entries")

def listBlackList():
    """ Retrieves the current blacklisted entries from the appliance firewall using the REST API

    """
    client = getBouncerApiSdkClient()
    try:
        response = client.blacklist_ip_addresses.list()
        return response
    except APIException as exception:
        print("unable to list blacklist entries")

#now call the register new user and the rest of the methods
registerNewUser()
response = addBlackList("192.168.1.1")
blacklists = listBlackList()
print("Listing blacklisted entries")
print(blacklists.ip_addresses)
if (response != None):
    # Note removing the blacklist only marks the entry as removed, the appliance will purge the record when
    # the scheduling service is run 
    removeBlackList(response, "192.168.1.1")
print("Listing blacklisted entries")
print(blacklists.ip_addresses)

