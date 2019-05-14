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

The generated code uses a few Maven dependencies e.g., Jackson, UniRest,
and Apache HttpClient. The reference to these dependencies is already
added in the pom.xml file will be installed automatically. Therefore,
you will need internet access for a successful build.

* In order to open the client library in Eclipse click on ``` File -> Import ```.

![Importing SDK into Eclipse - Step 1](https://apidocs.io/illustration/java?step=import0&workspaceFolder=Bouncer%20API-Java&workspaceName=BouncerAPI&projectName=BouncerAPILib&rootNamespace=com.example.www)

* In the import dialog, select ``` Existing Java Project ``` and click ``` Next ```.

![Importing SDK into Eclipse - Step 2](https://apidocs.io/illustration/java?step=import1&workspaceFolder=Bouncer%20API-Java&workspaceName=BouncerAPI&projectName=BouncerAPILib&rootNamespace=com.example.www)

* Browse to locate the folder containing the source code. Select the detected location of the project and click ``` Finish ```.

![Importing SDK into Eclipse - Step 3](https://apidocs.io/illustration/java?step=import2&workspaceFolder=Bouncer%20API-Java&workspaceName=BouncerAPI&projectName=BouncerAPILib&rootNamespace=com.example.www)

* Upon successful import, the project will be automatically built by Eclipse after automatically resolving the dependencies.

![Importing SDK into Eclipse - Step 4](https://apidocs.io/illustration/java?step=import3&workspaceFolder=Bouncer%20API-Java&workspaceName=BouncerAPI&projectName=BouncerAPILib&rootNamespace=com.example.www)

## How to Use

The following section explains how to use the BouncerAPI library in a new console project.

### 1. Starting a new project

For starting a new project, click the menu command ``` File > New > Project ```.

![Add a new project in Eclipse](https://apidocs.io/illustration/java?step=createNewProject0&workspaceFolder=Bouncer%20API-Java&workspaceName=BouncerAPI&projectName=BouncerAPILib&rootNamespace=com.example.www)

Next, choose ``` Maven > Maven Project ```and click ``` Next ```.

![Create a new Maven Project - Step 1](https://apidocs.io/illustration/java?step=createNewProject1&workspaceFolder=Bouncer%20API-Java&workspaceName=BouncerAPI&projectName=BouncerAPILib&rootNamespace=com.example.www)

Here, make sure to use the current workspace by choosing ``` Use default Workspace location ```, as shown in the picture below and click ``` Next ```.

![Create a new Maven Project - Step 2](https://apidocs.io/illustration/java?step=createNewProject2&workspaceFolder=Bouncer%20API-Java&workspaceName=BouncerAPI&projectName=BouncerAPILib&rootNamespace=com.example.www)

Following this, select the *quick start* project type to create a simple project with an existing class and a ``` main ``` method. To do this, choose ``` maven-archetype-quickstart ``` item from the list and click ``` Next ```.

![Create a new Maven Project - Step 3](https://apidocs.io/illustration/java?step=createNewProject3&workspaceFolder=Bouncer%20API-Java&workspaceName=BouncerAPI&projectName=BouncerAPILib&rootNamespace=com.example.www)

In the last step, provide a ``` Group Id ``` and ``` Artifact Id ``` as shown in the picture below and click ``` Finish ```.

![Create a new Maven Project - Step 4](https://apidocs.io/illustration/java?step=createNewProject4&workspaceFolder=Bouncer%20API-Java&workspaceName=BouncerAPI&projectName=BouncerAPILib&rootNamespace=com.example.www)

### 2. Add reference of the library project

The created Maven project manages its dependencies using its ``` pom.xml ``` file. In order to add a dependency on the *BouncerAPILib* client library, double click on the ``` pom.xml ``` file in the ``` Package Explorer ```. Opening the ``` pom.xml ``` file will render a graphical view on the cavas. Here, switch to the ``` Dependencies ``` tab and click the ``` Add ``` button as shown in the picture below.

![Adding dependency to the client library - Step 1](https://apidocs.io/illustration/java?step=testProject0&workspaceFolder=Bouncer%20API-Java&workspaceName=BouncerAPI&projectName=BouncerAPILib&rootNamespace=com.example.www)

Clicking the ``` Add ``` button will open a dialog where you need to specify BouncerAPI in ``` Group Id ``` and BouncerAPILib in the ``` Artifact Id ``` fields. Once added click ``` OK ```. Save the ``` pom.xml ``` file.

![Adding dependency to the client library - Step 2](https://apidocs.io/illustration/java?step=testProject1&workspaceFolder=Bouncer%20API-Java&workspaceName=BouncerAPI&projectName=BouncerAPILib&rootNamespace=com.example.www)

### 3. Write sample code

Once the ``` SimpleConsoleApp ``` is created, a file named ``` App.java ``` will be visible in the *Package Explorer* with a ``` main ``` method. This is the entry point for the execution of the created project.
Here, you can add code to initialize the client library and instantiate a *Controller* class. Sample code to initialize the client library and using controller methods is given in the subsequent sections.

![Adding dependency to the client library - Step 2](https://apidocs.io/illustration/java?step=testProject2&workspaceFolder=Bouncer%20API-Java&workspaceName=BouncerAPI&projectName=BouncerAPILib&rootNamespace=com.example.www)

## How to Test

The generated code and the server can be tested using automatically generated test cases. 
JUnit is used as the testing framework and test runner.

In Eclipse, for running the tests do the following:

1. Select the project *BouncerAPILib* from the package explorer.
2. Select "Run -> Run as -> JUnit Test" or use "Alt + Shift + X" followed by "T" to run the Tests.

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

API client can be initialized as following.

```java

BouncerAPIClient client = new BouncerAPIClient();
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

## <a name="blacklist_controller"></a>![Class: ](https://apidocs.io/img/class.png "com.example.www.controllers.BlacklistController") BlacklistController

### Get singleton instance

The singleton instance of the ``` BlacklistController ``` class can be accessed from the API Client.

```java
BlacklistController blacklist = client.getBlacklist();
```

### <a name="all_contents_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.BlacklistController.allContentsAsync") allContentsAsync

> This will list the entire contents of the Whitelist including both IP Addresses and Geo Locations.


```java
void allContentsAsync(final APICallBack<AllContentsResponse> callBack)
```

#### Example Usage

```java
// Invoking the API call with sample inputs
blacklist.allContentsAsync(new APICallBack<AllContentsResponse>() {
    public void onSuccess(HttpContext context, AllContentsResponse response) {
        // TODO success callback handler
    }
    public void onFailure(HttpContext context, Throwable error) {
        // TODO failure callback handler
    }
});

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



[Back to List of Controllers](#list_of_controllers)

## <a name="users_login_registration_controller"></a>![Class: ](https://apidocs.io/img/class.png "com.example.www.controllers.UsersLoginRegistrationController") UsersLoginRegistrationController

### Get singleton instance

The singleton instance of the ``` UsersLoginRegistrationController ``` class can be accessed from the API Client.

```java
UsersLoginRegistrationController usersLoginRegistration = client.getUsersLoginRegistration();
```

### <a name="login_to_bouncer_api_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.UsersLoginRegistrationController.loginToBouncerAPIAsync") loginToBouncerAPIAsync

> Authenticate to this Bouncer instance.


```java
void loginToBouncerAPIAsync(
        final LoginToBouncerAPIRequest body,
        final APICallBack<LoginToBouncerAPIResponse> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```java
try {
    LoginToBouncerAPIRequest body = new LoginToBouncerAPIRequest();
    // Invoking the API call with sample inputs
    usersLoginRegistration.loginToBouncerAPIAsync(body, new APICallBack<LoginToBouncerAPIResponse>() {
        public void onSuccess(HttpContext context, LoginToBouncerAPIResponse response) {
            // TODO success callback handler
        }
        public void onFailure(HttpContext context, Throwable error) {
            // TODO failure callback handler
        }
    });
} catch(JsonProcessingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="register_new_user_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.UsersLoginRegistrationController.registerNewUserAsync") registerNewUserAsync

> ONLY AVAILABLE when Bouncer is started with the `--testing` parameter.
> 
> Register a new user with this instance of Bouncer.


```java
void registerNewUserAsync(
        final RegisterNewUserRequest body,
        final APICallBack<RegisterNewUserResponse> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```java
try {
    RegisterNewUserRequest body = new RegisterNewUserRequest();
    // Invoking the API call with sample inputs
    usersLoginRegistration.registerNewUserAsync(body, new APICallBack<RegisterNewUserResponse>() {
        public void onSuccess(HttpContext context, RegisterNewUserResponse response) {
            // TODO success callback handler
        }
        public void onFailure(HttpContext context, Throwable error) {
            // TODO failure callback handler
        }
    });
} catch(JsonProcessingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



[Back to List of Controllers](#list_of_controllers)

## <a name="whitelist_geo_locations_controller"></a>![Class: ](https://apidocs.io/img/class.png "com.example.www.controllers.WhitelistGeoLocationsController") WhitelistGeoLocationsController

### Get singleton instance

The singleton instance of the ``` WhitelistGeoLocationsController ``` class can be accessed from the API Client.

```java
WhitelistGeoLocationsController whitelistGeoLocations = client.getWhitelistGeoLocations();
```

### <a name="remove_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.WhitelistGeoLocationsController.removeAsync") removeAsync

> Remove a Geo Location in the Whitelist


```java
void removeAsync(
        final String entryId,
        final GeoLocation body,
        final APICallBack<RemoveResponse1> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```java
try {
    String entryId = "entry_id";
    GeoLocation body = new GeoLocation();
    // Invoking the API call with sample inputs
    whitelistGeoLocations.removeAsync(entryId, body, new APICallBack<RemoveResponse1>() {
        public void onSuccess(HttpContext context, RemoveResponse1 response) {
            // TODO success callback handler
        }
        public void onFailure(HttpContext context, Throwable error) {
            // TODO failure callback handler
        }
    });
} catch(JsonProcessingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="update_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.WhitelistGeoLocationsController.updateAsync") updateAsync

> Update a Geo Location in the Whitelist


```java
void updateAsync(
        final String entryId,
        final GeoLocation body,
        final APICallBack<UpdateResponse1> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```java
try {
    String entryId = "entry_id";
    GeoLocation body = new GeoLocation();
    // Invoking the API call with sample inputs
    whitelistGeoLocations.updateAsync(entryId, body, new APICallBack<UpdateResponse1>() {
        public void onSuccess(HttpContext context, UpdateResponse1 response) {
            // TODO success callback handler
        }
        public void onFailure(HttpContext context, Throwable error) {
            // TODO failure callback handler
        }
    });
} catch(JsonProcessingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="create_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.WhitelistGeoLocationsController.createAsync") createAsync

> Create a Geo Location in the Whitelist. When POSTed-to this endpoint, Bouncer scans `geolist.txt` for any IPs matching the Country Code (CC) in the POSTed object and, for each: Bouncer will create a new ipaddress in this list (black- or white-list).


```java
void createAsync(
        final GeoLocation body,
        final APICallBack<CreateResponse1> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```java
try {
    GeoLocation body = new GeoLocation();
    // Invoking the API call with sample inputs
    whitelistGeoLocations.createAsync(body, new APICallBack<CreateResponse1>() {
        public void onSuccess(HttpContext context, CreateResponse1 response) {
            // TODO success callback handler
        }
        public void onFailure(HttpContext context, Throwable error) {
            // TODO failure callback handler
        }
    });
} catch(JsonProcessingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="get_details_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.WhitelistGeoLocationsController.getDetailsAsync") getDetailsAsync

> Get Details of a Geo Location Entry in the Whitelist


```java
void getDetailsAsync(
        final String entryId,
        final APICallBack<GetDetailsResponse1> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |


#### Example Usage

```java
String entryId = "884d9804999fc47a3c2694e49ad2536a";
// Invoking the API call with sample inputs
whitelistGeoLocations.getDetailsAsync(entryId, new APICallBack<GetDetailsResponse1>() {
    public void onSuccess(HttpContext context, GetDetailsResponse1 response) {
        // TODO success callback handler
    }
    public void onFailure(HttpContext context, Throwable error) {
        // TODO failure callback handler
    }
});

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="list_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.WhitelistGeoLocationsController.listAsync") listAsync

> List all Geo Locations in the Whitelist


```java
void listAsync(final APICallBack<ListResponse1> callBack)
```

#### Example Usage

```java
// Invoking the API call with sample inputs
whitelistGeoLocations.listAsync(new APICallBack<ListResponse1>() {
    public void onSuccess(HttpContext context, ListResponse1 response) {
        // TODO success callback handler
    }
    public void onFailure(HttpContext context, Throwable error) {
        // TODO failure callback handler
    }
});

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



[Back to List of Controllers](#list_of_controllers)

## <a name="blacklist_geo_locations_controller"></a>![Class: ](https://apidocs.io/img/class.png "com.example.www.controllers.BlacklistGeoLocationsController") BlacklistGeoLocationsController

### Get singleton instance

The singleton instance of the ``` BlacklistGeoLocationsController ``` class can be accessed from the API Client.

```java
BlacklistGeoLocationsController blacklistGeoLocations = client.getBlacklistGeoLocations();
```

### <a name="remove_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.BlacklistGeoLocationsController.removeAsync") removeAsync

> Remove a Geo Location in the Blacklist


```java
void removeAsync(
        final String entryId,
        final GeoLocation body,
        final APICallBack<RemoveResponse1> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```java
try {
    String entryId = "entry_id";
    GeoLocation body = new GeoLocation();
    // Invoking the API call with sample inputs
    blacklistGeoLocations.removeAsync(entryId, body, new APICallBack<RemoveResponse1>() {
        public void onSuccess(HttpContext context, RemoveResponse1 response) {
            // TODO success callback handler
        }
        public void onFailure(HttpContext context, Throwable error) {
            // TODO failure callback handler
        }
    });
} catch(JsonProcessingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="create_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.BlacklistGeoLocationsController.createAsync") createAsync

> Create a Geo Location in the Blacklist. When POSTed-to this endpoint, Bouncer scans `geolist.txt` for any IPs matching the Country Code (CC) in the POSTed object and, for each: Bouncer will create a new ipaddress in this list (black- or white-list).


```java
void createAsync(
        final GeoLocation body,
        final APICallBack<CreateResponse1> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```java
try {
    GeoLocation body = new GeoLocation();
    // Invoking the API call with sample inputs
    blacklistGeoLocations.createAsync(body, new APICallBack<CreateResponse1>() {
        public void onSuccess(HttpContext context, CreateResponse1 response) {
            // TODO success callback handler
        }
        public void onFailure(HttpContext context, Throwable error) {
            // TODO failure callback handler
        }
    });
} catch(JsonProcessingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="update_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.BlacklistGeoLocationsController.updateAsync") updateAsync

> Update a Geo Location in the Blacklist


```java
void updateAsync(
        final String entryId,
        final GeoLocation body,
        final APICallBack<UpdateResponse1> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```java
try {
    String entryId = "entry_id";
    GeoLocation body = new GeoLocation();
    // Invoking the API call with sample inputs
    blacklistGeoLocations.updateAsync(entryId, body, new APICallBack<UpdateResponse1>() {
        public void onSuccess(HttpContext context, UpdateResponse1 response) {
            // TODO success callback handler
        }
        public void onFailure(HttpContext context, Throwable error) {
            // TODO failure callback handler
        }
    });
} catch(JsonProcessingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="list_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.BlacklistGeoLocationsController.listAsync") listAsync

> List all Geo Locations in the Blacklist


```java
void listAsync(final APICallBack<ListResponse1> callBack)
```

#### Example Usage

```java
// Invoking the API call with sample inputs
blacklistGeoLocations.listAsync(new APICallBack<ListResponse1>() {
    public void onSuccess(HttpContext context, ListResponse1 response) {
        // TODO success callback handler
    }
    public void onFailure(HttpContext context, Throwable error) {
        // TODO failure callback handler
    }
});

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="get_details_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.BlacklistGeoLocationsController.getDetailsAsync") getDetailsAsync

> Get Details of a Geo Location Entry in the Blacklist


```java
void getDetailsAsync(
        final String entryId,
        final APICallBack<GetDetailsResponse1> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |


#### Example Usage

```java
String entryId = "884d9804999fc47a3c2694e49ad2536a";
// Invoking the API call with sample inputs
blacklistGeoLocations.getDetailsAsync(entryId, new APICallBack<GetDetailsResponse1>() {
    public void onSuccess(HttpContext context, GetDetailsResponse1 response) {
        // TODO success callback handler
    }
    public void onFailure(HttpContext context, Throwable error) {
        // TODO failure callback handler
    }
});

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



[Back to List of Controllers](#list_of_controllers)

## <a name="check_ip_addresses_controller"></a>![Class: ](https://apidocs.io/img/class.png "com.example.www.controllers.CheckIPAddressesController") CheckIPAddressesController

### Get singleton instance

The singleton instance of the ``` CheckIPAddressesController ``` class can be accessed from the API Client.

```java
CheckIPAddressesController checkIPAddresses = client.getCheckIPAddresses();
```

### <a name="test_for_list_membership_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.CheckIPAddressesController.testForListMembershipAsync") testForListMembershipAsync

> Check if an IP Address is Already White- or Black-Listed


```java
void testForListMembershipAsync(
        final String ipAddress,
        final APICallBack<TestForListMembershipResponse> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| ipAddress |  ``` Required ```  | the IP address to check |


#### Example Usage

```java
String ipAddress = "192.168.100.14";
// Invoking the API call with sample inputs
checkIPAddresses.testForListMembershipAsync(ipAddress, new APICallBack<TestForListMembershipResponse>() {
    public void onSuccess(HttpContext context, TestForListMembershipResponse response) {
        // TODO success callback handler
    }
    public void onFailure(HttpContext context, Throwable error) {
        // TODO failure callback handler
    }
});

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



[Back to List of Controllers](#list_of_controllers)

## <a name="blacklist_ip_addresses_controller"></a>![Class: ](https://apidocs.io/img/class.png "com.example.www.controllers.BlacklistIPAddressesController") BlacklistIPAddressesController

### Get singleton instance

The singleton instance of the ``` BlacklistIPAddressesController ``` class can be accessed from the API Client.

```java
BlacklistIPAddressesController blacklistIPAddresses = client.getBlacklistIPAddresses();
```

### <a name="update_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.BlacklistIPAddressesController.updateAsync") updateAsync

> Update an IP Address in the Blacklist


```java
void updateAsync(
        final String entryId,
        final IPAddress body,
        final APICallBack<UpdateResponse> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```java
try {
    String entryId = "entry_id";
    IPAddress body = new IPAddress();
    // Invoking the API call with sample inputs
    blacklistIPAddresses.updateAsync(entryId, body, new APICallBack<UpdateResponse>() {
        public void onSuccess(HttpContext context, UpdateResponse response) {
            // TODO success callback handler
        }
        public void onFailure(HttpContext context, Throwable error) {
            // TODO failure callback handler
        }
    });
} catch(JsonProcessingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="remove_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.BlacklistIPAddressesController.removeAsync") removeAsync

> Remove an IP Address in the Blacklist


```java
void removeAsync(
        final String entryId,
        final IPAddress body,
        final APICallBack<RemoveResponse> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```java
try {
    String entryId = "entry_id";
    IPAddress body = new IPAddress();
    // Invoking the API call with sample inputs
    blacklistIPAddresses.removeAsync(entryId, body, new APICallBack<RemoveResponse>() {
        public void onSuccess(HttpContext context, RemoveResponse response) {
            // TODO success callback handler
        }
        public void onFailure(HttpContext context, Throwable error) {
            // TODO failure callback handler
        }
    });
} catch(JsonProcessingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="get_details_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.BlacklistIPAddressesController.getDetailsAsync") getDetailsAsync

> Get Details of an IP Address Entry in the Blacklist


```java
void getDetailsAsync(
        final String entryId,
        final APICallBack<GetDetailsResponse> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |


#### Example Usage

```java
String entryId = "884d9804999fc47a3c2694e49ad2536a";
// Invoking the API call with sample inputs
blacklistIPAddresses.getDetailsAsync(entryId, new APICallBack<GetDetailsResponse>() {
    public void onSuccess(HttpContext context, GetDetailsResponse response) {
        // TODO success callback handler
    }
    public void onFailure(HttpContext context, Throwable error) {
        // TODO failure callback handler
    }
});

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="create_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.BlacklistIPAddressesController.createAsync") createAsync

> Create an IP Address in the Blacklist


```java
void createAsync(
        final IPAddress body,
        final APICallBack<CreateResponse> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```java
try {
    IPAddress body = new IPAddress();
    // Invoking the API call with sample inputs
    blacklistIPAddresses.createAsync(body, new APICallBack<CreateResponse>() {
        public void onSuccess(HttpContext context, CreateResponse response) {
            // TODO success callback handler
        }
        public void onFailure(HttpContext context, Throwable error) {
            // TODO failure callback handler
        }
    });
} catch(JsonProcessingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="search_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.BlacklistIPAddressesController.searchAsync") searchAsync

> Search for IP Addresses in the Blacklist


```java
void searchAsync(
        final String searchFilter,
        final APICallBack<SearchResponse> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| searchFilter |  ``` Required ```  | an comma-separated lsit of IP addresses in CIDR format (`192.168.100.14/24`) except with `/` replaced by `+` |


#### Example Usage

```java
String searchFilter = "192.168.100.0+24,192.168.101.0+24";
// Invoking the API call with sample inputs
blacklistIPAddresses.searchAsync(searchFilter, new APICallBack<SearchResponse>() {
    public void onSuccess(HttpContext context, SearchResponse response) {
        // TODO success callback handler
    }
    public void onFailure(HttpContext context, Throwable error) {
        // TODO failure callback handler
    }
});

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="list_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.BlacklistIPAddressesController.listAsync") listAsync

> List all IP Addresses in the Blacklist


```java
void listAsync(final APICallBack<ListResponse> callBack)
```

#### Example Usage

```java
// Invoking the API call with sample inputs
blacklistIPAddresses.listAsync(new APICallBack<ListResponse>() {
    public void onSuccess(HttpContext context, ListResponse response) {
        // TODO success callback handler
    }
    public void onFailure(HttpContext context, Throwable error) {
        // TODO failure callback handler
    }
});

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



[Back to List of Controllers](#list_of_controllers)

## <a name="whitelist_ip_addresses_controller"></a>![Class: ](https://apidocs.io/img/class.png "com.example.www.controllers.WhitelistIPAddressesController") WhitelistIPAddressesController

### Get singleton instance

The singleton instance of the ``` WhitelistIPAddressesController ``` class can be accessed from the API Client.

```java
WhitelistIPAddressesController whitelistIPAddresses = client.getWhitelistIPAddresses();
```

### <a name="remove_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.WhitelistIPAddressesController.removeAsync") removeAsync

> Remove an IP Address in the Whitelist


```java
void removeAsync(
        final String entryId,
        final IPAddress body,
        final APICallBack<RemoveResponse> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```java
try {
    String entryId = "entry_id";
    IPAddress body = new IPAddress();
    // Invoking the API call with sample inputs
    whitelistIPAddresses.removeAsync(entryId, body, new APICallBack<RemoveResponse>() {
        public void onSuccess(HttpContext context, RemoveResponse response) {
            // TODO success callback handler
        }
        public void onFailure(HttpContext context, Throwable error) {
            // TODO failure callback handler
        }
    });
} catch(JsonProcessingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="update_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.WhitelistIPAddressesController.updateAsync") updateAsync

> Update an IP Address in the Whitelist


```java
void updateAsync(
        final String entryId,
        final IPAddress body,
        final APICallBack<UpdateResponse> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```java
try {
    String entryId = "entry_id";
    IPAddress body = new IPAddress();
    // Invoking the API call with sample inputs
    whitelistIPAddresses.updateAsync(entryId, body, new APICallBack<UpdateResponse>() {
        public void onSuccess(HttpContext context, UpdateResponse response) {
            // TODO success callback handler
        }
        public void onFailure(HttpContext context, Throwable error) {
            // TODO failure callback handler
        }
    });
} catch(JsonProcessingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="create_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.WhitelistIPAddressesController.createAsync") createAsync

> Create an IP Address in the Whitelist


```java
void createAsync(
        final IPAddress body,
        final APICallBack<CreateResponse> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```java
try {
    IPAddress body = new IPAddress();
    // Invoking the API call with sample inputs
    whitelistIPAddresses.createAsync(body, new APICallBack<CreateResponse>() {
        public void onSuccess(HttpContext context, CreateResponse response) {
            // TODO success callback handler
        }
        public void onFailure(HttpContext context, Throwable error) {
            // TODO failure callback handler
        }
    });
} catch(JsonProcessingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="get_details_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.WhitelistIPAddressesController.getDetailsAsync") getDetailsAsync

> Get Details of an IP Address Entry in the Whitelist


```java
void getDetailsAsync(
        final String entryId,
        final APICallBack<GetDetailsResponse> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |


#### Example Usage

```java
String entryId = "884d9804999fc47a3c2694e49ad2536a";
// Invoking the API call with sample inputs
whitelistIPAddresses.getDetailsAsync(entryId, new APICallBack<GetDetailsResponse>() {
    public void onSuccess(HttpContext context, GetDetailsResponse response) {
        // TODO success callback handler
    }
    public void onFailure(HttpContext context, Throwable error) {
        // TODO failure callback handler
    }
});

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="list_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.WhitelistIPAddressesController.listAsync") listAsync

> List all IP Addresses in the Whitelist


```java
void listAsync(final APICallBack<ListResponse> callBack)
```

#### Example Usage

```java
// Invoking the API call with sample inputs
whitelistIPAddresses.listAsync(new APICallBack<ListResponse>() {
    public void onSuccess(HttpContext context, ListResponse response) {
        // TODO success callback handler
    }
    public void onFailure(HttpContext context, Throwable error) {
        // TODO failure callback handler
    }
});

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



### <a name="search_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.WhitelistIPAddressesController.searchAsync") searchAsync

> Search for IP Addresses in the Whitelist


```java
void searchAsync(
        final String searchFilter,
        final APICallBack<SearchResponse> callBack)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| searchFilter |  ``` Required ```  | an comma-separated lsit of IP addresses in CIDR format (`192.168.100.14/24`) except with `/` replaced by `+` |


#### Example Usage

```java
String searchFilter = "192.168.100.0+24,192.168.101.0+24";
// Invoking the API call with sample inputs
whitelistIPAddresses.searchAsync(searchFilter, new APICallBack<SearchResponse>() {
    public void onSuccess(HttpContext context, SearchResponse response) {
        // TODO success callback handler
    }
    public void onFailure(HttpContext context, Throwable error) {
        // TODO failure callback handler
    }
});

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



[Back to List of Controllers](#list_of_controllers)

## <a name="whitelist_controller"></a>![Class: ](https://apidocs.io/img/class.png "com.example.www.controllers.WhitelistController") WhitelistController

### Get singleton instance

The singleton instance of the ``` WhitelistController ``` class can be accessed from the API Client.

```java
WhitelistController whitelist = client.getWhitelist();
```

### <a name="all_contents_async"></a>![Method: ](https://apidocs.io/img/method.png "com.example.www.controllers.WhitelistController.allContentsAsync") allContentsAsync

> This will list the entire contents of the Whitelist including both IP Addresses and Geo Locations.


```java
void allContentsAsync(final APICallBack<AllContentsResponse> callBack)
```

#### Example Usage

```java
// Invoking the API call with sample inputs
whitelist.allContentsAsync(new APICallBack<AllContentsResponse>() {
    public void onSuccess(HttpContext context, AllContentsResponse response) {
        // TODO success callback handler
    }
    public void onFailure(HttpContext context, Throwable error) {
        // TODO failure callback handler
    }
});

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |



[Back to List of Controllers](#list_of_controllers)



