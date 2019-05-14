# Getting started

![Bouncer Logo](https://raw.githubusercontent.com/nmfta-repo/nmfta-bouncer/master/project-bouncer-small.png)

The API for the bouncer firewall appliance, automating blacklisting via `ufw`. See https://github.com/nmfta-repo/nmfta-bouncer for the server code.

The version documented here is API version `1.1`. All endpoints below have a `/v1.1/` leading path element.

## Authentication

This API uses Custom HTTP Header Bearer-token authentication. The following headers are required to be sent with each request

```http
Authorization: Bearer {access token from /login}
```

## Working with Date and Time

Dates and times in the API are treated as opaque data types at present. Any date-time format can be used as long as the code consuming it is consistent with the code populating it.

We recommend all times in UTC, formatted using ISO 8601 string (format `yyyy-MM-ddTHH:mm:ss.fffZ`).

## Error Codes

Errors in this API are returned in JSON objects with error code references in an `Error` field. If an endpoint returns a status code other than `200` then it will return a JSON error object indicating the error in `Error` field. No descriptions of the error will be provided, client code or developers need to consult the table here to understand the value in the `Error` field.

| Endpoint                                   | Error Code | Description                                                                           |
|:-------------------------------------------|:----------:|:--------------------------------------------------------------------------------------|
| `/register`                                | 1001       | User Name is required                                                                 |
|                                            | 1002       | Password is required                                                                  |
|                                            | 1003       | Duplicate User Name / User already exists                                             |
|                                            | 1004       | User name too long                                                                    |
|                                            | 1005       | Invalid Password                                                                      |
| `/login`                                   | 2000       | Missing User Name                                                                     |
|                                            | 2001       | Missing Password                                                                      |
|                                            | 2002       | Missing Grant type                                                                    |
|                                            | 2003       | Invalid User or password is not valid                                                 |
| `/whitelists/IPAddresses/create`           | 3000       | IPv4 or IPv6 is required                                                              |
|                                            | 3001       | IP Address is invalid                                                                 |
|                                            | 3002       | Start Date is required                                                                |
|                                            | 3003       | Start Date is invalid                                                                 |
|                                            | 3004       | End Date is required                                                                  |
|                                            | 3005       | End Date is invalid                                                                   |
|                                            | 3006       | End Date needs to be greater than Start Date                                          |
|                                            | 3007       | Comments too long (restrict to 3000 characters or less)                               |
|                                            | 3008       | IP Address already whitelisted                                                        |
|                                            | 3009       | IP Address currently blacklisted, remove it from blacklist before adding to whitelist |
| `/blacklists/IPAddresses/create`           | 4000       | IPv4 or IPv6 is required                                                              |
|                                            | 4001       | IP Address is invalid                                                                 |
|                                            | 4002       | Start Date is required                                                                |
|                                            | 4003       | Start Date is invalid                                                                 |
|                                            | 4004       | End Date is required                                                                  |
|                                            | 4005       | End Date is invalid                                                                   |
|                                            | 4006       | End Date needs to be greater than Start Date                                          |
|                                            | 4007       | Comments too long (restrict to 3000 characters or less)                               |
|                                            | 4008       | IP Address already blacklisted                                                        |
|                                            | 4009       | IP Address currently whitelisted, remove it from whitelist before adding to blacklist |
|`/whitelists/ipaddresses/{entry_ id}/delete`| 5000       | Entry Id is required and should be an integer                                         |
|                                            | 5001       | Entry Id not found                                                                    |
| `/blacklists/ipaddresses/{entry_id}/delete`| 6000       | Entry Id is required and should be an integer                                         |
|                                            | 6001       | Entry Id not found                                                                    |

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=Bouncer%20API-Python)


## How to Use

The following section explains how to use the Bouncerapi SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=Bouncer%20API-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=Bouncer%20API-Python&projectName=bouncerapi)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=Bouncer%20API-Python&projectName=bouncerapi)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=Bouncer%20API-Python&projectName=bouncerapi)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from bouncerapi.bouncerapi_client import BouncerapiClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Bouncer%20API-Python&libraryName=bouncerapi.bouncerapi_client&projectName=bouncerapi&className=BouncerapiClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=Bouncer%20API-Python&libraryName=bouncerapi.bouncerapi_client&projectName=bouncerapi&className=BouncerapiClient)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

API client can be initialized as following.

```python

client = BouncerapiClient()
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [BlacklistController](#blacklist_controller)
* [UsersLoginRegistrationController](#users_login_registration_controller)
* [WhitelistGeoLocationsController](#whitelist_geo_locations_controller)
* [BlacklistGeoLocationsController](#blacklist_geo_locations_controller)
* [CheckIPAddressesController](#check_ip_addresses_controller)
* [BlacklistIPAddressesController](#blacklist_ip_addresses_controller)
* [WhitelistIPAddressesController](#whitelist_ip_addresses_controller)
* [WhitelistController](#whitelist_controller)

## <a name="blacklist_controller"></a>![Class: ](https://apidocs.io/img/class.png ".BlacklistController") BlacklistController

### Get controller instance

An instance of the ``` BlacklistController ``` class can be accessed from the API Client.

```python
 blacklist_controller = client.blacklist
```

### <a name="all_contents"></a>![Method: ](https://apidocs.io/img/method.png ".BlacklistController.all_contents") all_contents

> This will list the entire contents of the Whitelist including both IP Addresses and Geo Locations.

```python
def all_contents(self)
```

#### Example Usage

```python

result = blacklist_controller.all_contents()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




[Back to List of Controllers](#list_of_controllers)

## <a name="users_login_registration_controller"></a>![Class: ](https://apidocs.io/img/class.png ".UsersLoginRegistrationController") UsersLoginRegistrationController

### Get controller instance

An instance of the ``` UsersLoginRegistrationController ``` class can be accessed from the API Client.

```python
 users_login_registration_controller = client.users_login_registration
```

### <a name="login_to_bouncer_api"></a>![Method: ](https://apidocs.io/img/method.png ".UsersLoginRegistrationController.login_to_bouncer_api") login_to_bouncer_api

> Authenticate to this Bouncer instance.

```python
def login_to_bouncer_api(self,
                             body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = LoginToBouncerAPIRequest()

result = users_login_registration_controller.login_to_bouncer_api(body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="register_new_user"></a>![Method: ](https://apidocs.io/img/method.png ".UsersLoginRegistrationController.register_new_user") register_new_user

> ONLY AVAILABLE when Bouncer is started with the `--testing` parameter.
> 
> Register a new user with this instance of Bouncer.

```python
def register_new_user(self,
                          body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = RegisterNewUserRequest()

result = users_login_registration_controller.register_new_user(body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




[Back to List of Controllers](#list_of_controllers)

## <a name="whitelist_geo_locations_controller"></a>![Class: ](https://apidocs.io/img/class.png ".WhitelistGeoLocationsController") WhitelistGeoLocationsController

### Get controller instance

An instance of the ``` WhitelistGeoLocationsController ``` class can be accessed from the API Client.

```python
 whitelist_geo_locations_controller = client.whitelist_geo_locations
```

### <a name="remove"></a>![Method: ](https://apidocs.io/img/method.png ".WhitelistGeoLocationsController.remove") remove

> Remove a Geo Location in the Whitelist

```python
def remove(self,
                entry_id,
                body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
entry_id = 'entry_id'
body = GeoLocation()

result = whitelist_geo_locations_controller.remove(entry_id, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="update"></a>![Method: ](https://apidocs.io/img/method.png ".WhitelistGeoLocationsController.update") update

> Update a Geo Location in the Whitelist

```python
def update(self,
                entry_id,
                body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
entry_id = 'entry_id'
body = GeoLocation()

result = whitelist_geo_locations_controller.update(entry_id, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="create"></a>![Method: ](https://apidocs.io/img/method.png ".WhitelistGeoLocationsController.create") create

> Create a Geo Location in the Whitelist. When POSTed-to this endpoint, Bouncer scans `geolist.txt` for any IPs matching the Country Code (CC) in the POSTed object and, for each: Bouncer will create a new ipaddress in this list (black- or white-list).

```python
def create(self,
                body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = GeoLocation()

result = whitelist_geo_locations_controller.create(body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="get_details"></a>![Method: ](https://apidocs.io/img/method.png ".WhitelistGeoLocationsController.get_details") get_details

> Get Details of a Geo Location Entry in the Whitelist

```python
def get_details(self,
                    entry_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |



#### Example Usage

```python
entry_id = '884d9804999fc47a3c2694e49ad2536a'

result = whitelist_geo_locations_controller.get_details(entry_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="list"></a>![Method: ](https://apidocs.io/img/method.png ".WhitelistGeoLocationsController.list") list

> List all Geo Locations in the Whitelist

```python
def list(self)
```

#### Example Usage

```python

result = whitelist_geo_locations_controller.list()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




[Back to List of Controllers](#list_of_controllers)

## <a name="blacklist_geo_locations_controller"></a>![Class: ](https://apidocs.io/img/class.png ".BlacklistGeoLocationsController") BlacklistGeoLocationsController

### Get controller instance

An instance of the ``` BlacklistGeoLocationsController ``` class can be accessed from the API Client.

```python
 blacklist_geo_locations_controller = client.blacklist_geo_locations
```

### <a name="remove"></a>![Method: ](https://apidocs.io/img/method.png ".BlacklistGeoLocationsController.remove") remove

> Remove a Geo Location in the Blacklist

```python
def remove(self,
                entry_id,
                body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
entry_id = 'entry_id'
body = GeoLocation()

result = blacklist_geo_locations_controller.remove(entry_id, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="create"></a>![Method: ](https://apidocs.io/img/method.png ".BlacklistGeoLocationsController.create") create

> Create a Geo Location in the Blacklist. When POSTed-to this endpoint, Bouncer scans `geolist.txt` for any IPs matching the Country Code (CC) in the POSTed object and, for each: Bouncer will create a new ipaddress in this list (black- or white-list).

```python
def create(self,
                body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = GeoLocation()

result = blacklist_geo_locations_controller.create(body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="update"></a>![Method: ](https://apidocs.io/img/method.png ".BlacklistGeoLocationsController.update") update

> Update a Geo Location in the Blacklist

```python
def update(self,
                entry_id,
                body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
entry_id = 'entry_id'
body = GeoLocation()

result = blacklist_geo_locations_controller.update(entry_id, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="list"></a>![Method: ](https://apidocs.io/img/method.png ".BlacklistGeoLocationsController.list") list

> List all Geo Locations in the Blacklist

```python
def list(self)
```

#### Example Usage

```python

result = blacklist_geo_locations_controller.list()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="get_details"></a>![Method: ](https://apidocs.io/img/method.png ".BlacklistGeoLocationsController.get_details") get_details

> Get Details of a Geo Location Entry in the Blacklist

```python
def get_details(self,
                    entry_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |



#### Example Usage

```python
entry_id = '884d9804999fc47a3c2694e49ad2536a'

result = blacklist_geo_locations_controller.get_details(entry_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




[Back to List of Controllers](#list_of_controllers)

## <a name="check_ip_addresses_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CheckIPAddressesController") CheckIPAddressesController

### Get controller instance

An instance of the ``` CheckIPAddressesController ``` class can be accessed from the API Client.

```python
 check_ip_addresses_controller = client.check_ip_addresses
```

### <a name="test_for_list_membership"></a>![Method: ](https://apidocs.io/img/method.png ".CheckIPAddressesController.test_for_list_membership") test_for_list_membership

> Check if an IP Address is Already White- or Black-Listed

```python
def test_for_list_membership(self,
                                 ip_address)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| ipAddress |  ``` Required ```  | the IP address to check |



#### Example Usage

```python
ip_address = '192.168.100.14'

result = check_ip_addresses_controller.test_for_list_membership(ip_address)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




[Back to List of Controllers](#list_of_controllers)

## <a name="blacklist_ip_addresses_controller"></a>![Class: ](https://apidocs.io/img/class.png ".BlacklistIPAddressesController") BlacklistIPAddressesController

### Get controller instance

An instance of the ``` BlacklistIPAddressesController ``` class can be accessed from the API Client.

```python
 blacklist_ip_addresses_controller = client.blacklist_ip_addresses
```

### <a name="update"></a>![Method: ](https://apidocs.io/img/method.png ".BlacklistIPAddressesController.update") update

> Update an IP Address in the Blacklist

```python
def update(self,
                entry_id,
                body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
entry_id = 'entry_id'
body = IPAddress()

result = blacklist_ip_addresses_controller.update(entry_id, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="remove"></a>![Method: ](https://apidocs.io/img/method.png ".BlacklistIPAddressesController.remove") remove

> Remove an IP Address in the Blacklist

```python
def remove(self,
                entry_id,
                body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
entry_id = 'entry_id'
body = IPAddress()

result = blacklist_ip_addresses_controller.remove(entry_id, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="get_details"></a>![Method: ](https://apidocs.io/img/method.png ".BlacklistIPAddressesController.get_details") get_details

> Get Details of an IP Address Entry in the Blacklist

```python
def get_details(self,
                    entry_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |



#### Example Usage

```python
entry_id = '884d9804999fc47a3c2694e49ad2536a'

result = blacklist_ip_addresses_controller.get_details(entry_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="create"></a>![Method: ](https://apidocs.io/img/method.png ".BlacklistIPAddressesController.create") create

> Create an IP Address in the Blacklist

```python
def create(self,
                body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = IPAddress()

result = blacklist_ip_addresses_controller.create(body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="search"></a>![Method: ](https://apidocs.io/img/method.png ".BlacklistIPAddressesController.search") search

> Search for IP Addresses in the Blacklist

```python
def search(self,
                search_filter)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| searchFilter |  ``` Required ```  | an comma-separated lsit of IP addresses in CIDR format (`192.168.100.14/24`) except with `/` replaced by `+` |



#### Example Usage

```python
search_filter = '192.168.100.0+24,192.168.101.0+24'

result = blacklist_ip_addresses_controller.search(search_filter)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="list"></a>![Method: ](https://apidocs.io/img/method.png ".BlacklistIPAddressesController.list") list

> List all IP Addresses in the Blacklist

```python
def list(self)
```

#### Example Usage

```python

result = blacklist_ip_addresses_controller.list()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




[Back to List of Controllers](#list_of_controllers)

## <a name="whitelist_ip_addresses_controller"></a>![Class: ](https://apidocs.io/img/class.png ".WhitelistIPAddressesController") WhitelistIPAddressesController

### Get controller instance

An instance of the ``` WhitelistIPAddressesController ``` class can be accessed from the API Client.

```python
 whitelist_ip_addresses_controller = client.whitelist_ip_addresses
```

### <a name="remove"></a>![Method: ](https://apidocs.io/img/method.png ".WhitelistIPAddressesController.remove") remove

> Remove an IP Address in the Whitelist

```python
def remove(self,
                entry_id,
                body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
entry_id = 'entry_id'
body = IPAddress()

result = whitelist_ip_addresses_controller.remove(entry_id, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="update"></a>![Method: ](https://apidocs.io/img/method.png ".WhitelistIPAddressesController.update") update

> Update an IP Address in the Whitelist

```python
def update(self,
                entry_id,
                body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
entry_id = 'entry_id'
body = IPAddress()

result = whitelist_ip_addresses_controller.update(entry_id, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="create"></a>![Method: ](https://apidocs.io/img/method.png ".WhitelistIPAddressesController.create") create

> Create an IP Address in the Whitelist

```python
def create(self,
                body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = IPAddress()

result = whitelist_ip_addresses_controller.create(body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="get_details"></a>![Method: ](https://apidocs.io/img/method.png ".WhitelistIPAddressesController.get_details") get_details

> Get Details of an IP Address Entry in the Whitelist

```python
def get_details(self,
                    entry_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |



#### Example Usage

```python
entry_id = '884d9804999fc47a3c2694e49ad2536a'

result = whitelist_ip_addresses_controller.get_details(entry_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="list"></a>![Method: ](https://apidocs.io/img/method.png ".WhitelistIPAddressesController.list") list

> List all IP Addresses in the Whitelist

```python
def list(self)
```

#### Example Usage

```python

result = whitelist_ip_addresses_controller.list()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="search"></a>![Method: ](https://apidocs.io/img/method.png ".WhitelistIPAddressesController.search") search

> Search for IP Addresses in the Whitelist

```python
def search(self,
                search_filter)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| searchFilter |  ``` Required ```  | an comma-separated lsit of IP addresses in CIDR format (`192.168.100.14/24`) except with `/` replaced by `+` |



#### Example Usage

```python
search_filter = '192.168.100.0+24,192.168.101.0+24'

result = whitelist_ip_addresses_controller.search(search_filter)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




[Back to List of Controllers](#list_of_controllers)

## <a name="whitelist_controller"></a>![Class: ](https://apidocs.io/img/class.png ".WhitelistController") WhitelistController

### Get controller instance

An instance of the ``` WhitelistController ``` class can be accessed from the API Client.

```python
 whitelist_controller = client.whitelist
```

### <a name="all_contents"></a>![Method: ](https://apidocs.io/img/method.png ".WhitelistController.all_contents") all_contents

> This will list the entire contents of the Whitelist including both IP Addresses and Geo Locations.

```python
def all_contents(self)
```

#### Example Usage

```python

result = whitelist_controller.all_contents()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




[Back to List of Controllers](#list_of_controllers)



