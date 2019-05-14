1) Setup Virtual environment => pip -m venv env
2) Activate Virtual Enviroment => .\env\Scripts\Activate
3) Install Requirements => pip Install -r requirements.txt
4) Install bouncer sdk from local => pip install ../../sdk/python
5) Update Bouncer Rest API DNS Host
6) Update User Name and Password in bouncer_client.py
7)   NOTE: Bouncer supports new registration only if the Bouncer Rest API was started in testing mode
8) update bouncerapi.configuration and add a Class Variable called ACCESS_TOKEN and set its value to None. The Value for this class Variable
is set in the getBouncerApiSdkClient() method in bouncer_client.py
9) Update bouncerapi.http.auth.custom_auth.py and add ACCESS_TOKEN to Authorization Header as "Bearer {ACCESS_TOKEN}"
            if (Configuration.ACCESS_TOKEN != None):
                http_request.headers["Authorization"] = "Bearer {}".format(Configuration.ACCESS_TOKEN)
10) Execute Application => python bouncer_client.py