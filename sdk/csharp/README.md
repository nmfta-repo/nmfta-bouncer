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

The generated code uses the Newtonsoft Json.NET NuGet Package. If the automatic NuGet package restore
is enabled, these dependencies will be installed automatically. Therefore,
you will need internet access for build.

"This library requires Visual Studio 2017 for compilation."
1. Open the solution (BouncerAPI.sln) file.
2. Invoke the build process using `Ctrl+Shift+B` shortcut key or using the `Build` menu as shown below.

![Building SDK using Visual Studio](https://apidocs.io/illustration/cs?step=buildSDK&workspaceFolder=Bouncer%20API-CSharp&workspaceName=BouncerAPI&projectName=BouncerAPI.Tests)

## How to Use

The build process generates a portable class library, which can be used like a normal class library. The generated library is compatible with Windows Forms, Windows RT, Windows Phone 8,
Silverlight 5, Xamarin iOS, Xamarin Android and Mono. More information on how to use can be found at the [MSDN Portable Class Libraries documentation](http://msdn.microsoft.com/en-us/library/vstudio/gg597391%28v=vs.100%29.aspx).

The following section explains how to use the BouncerAPI library in a new console project.

### 1. Starting a new project

For starting a new project, right click on the current solution from the *solution explorer* and choose  ``` Add -> New Project ```.

![Add a new project in the existing solution using Visual Studio](https://apidocs.io/illustration/cs?step=addProject&workspaceFolder=Bouncer%20API-CSharp&workspaceName=BouncerAPI&projectName=BouncerAPI.Tests)

Next, choose "Console Application", provide a ``` TestConsoleProject ``` as the project name and click ``` OK ```.

![Create a new console project using Visual Studio](https://apidocs.io/illustration/cs?step=createProject&workspaceFolder=Bouncer%20API-CSharp&workspaceName=BouncerAPI&projectName=BouncerAPI.Tests)

### 2. Set as startup project

The new console project is the entry point for the eventual execution. This requires us to set the ``` TestConsoleProject ``` as the start-up project. To do this, right-click on the  ``` TestConsoleProject ``` and choose  ``` Set as StartUp Project ``` form the context menu.

![Set the new cosole project as the start up project](https://apidocs.io/illustration/cs?step=setStartup&workspaceFolder=Bouncer%20API-CSharp&workspaceName=BouncerAPI&projectName=BouncerAPI.Tests)

### 3. Add reference of the library project

In order to use the BouncerAPI library in the new project, first we must add a projet reference to the ``` TestConsoleProject ```. First, right click on the ``` References ``` node in the *solution explorer* and click ``` Add Reference... ```.

![Open references of the TestConsoleProject](https://apidocs.io/illustration/cs?step=addReference&workspaceFolder=Bouncer%20API-CSharp&workspaceName=BouncerAPI&projectName=BouncerAPI.Tests)

Next, a window will be displayed where we must set the ``` checkbox ``` on ``` BouncerAPI.Tests ``` and click ``` OK ```. By doing this, we have added a reference of the ```BouncerAPI.Tests``` project into the new ``` TestConsoleProject ```.

![Add a reference to the TestConsoleProject](https://apidocs.io/illustration/cs?step=createReference&workspaceFolder=Bouncer%20API-CSharp&workspaceName=BouncerAPI&projectName=BouncerAPI.Tests)

### 4. Write sample code

Once the ``` TestConsoleProject ``` is created, a file named ``` Program.cs ``` will be visible in the *solution explorer* with an empty ``` Main ``` method. This is the entry point for the execution of the entire solution.
Here, you can add code to initialize the client library and acquire the instance of a *Controller* class. Sample code to initialize the client library and using controller methods is given in the subsequent sections.

![Add a reference to the TestConsoleProject](https://apidocs.io/illustration/cs?step=addCode&workspaceFolder=Bouncer%20API-CSharp&workspaceName=BouncerAPI&projectName=BouncerAPI.Tests)

## How to Test

The generated SDK also contain one or more Tests, which are contained in the Tests project.
In order to invoke these test cases, you will need *NUnit 3.0 Test Adapter Extension for Visual Studio*.
Once the SDK is complied, the test cases should appear in the Test Explorer window.
Here, you can click *Run All* to execute these test cases.

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

API client can be initialized as following.

```csharp

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

## <a name="blacklist_controller"></a>![Class: ](https://apidocs.io/img/class.png "BouncerAPI.Tests.Controllers.BlacklistController") BlacklistController

### Get singleton instance

The singleton instance of the ``` BlacklistController ``` class can be accessed from the API Client.

```csharp
BlacklistController blacklist = client.Blacklist;
```

### <a name="all_contents"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.BlacklistController.AllContents") AllContents

> This will list the entire contents of the Whitelist including both IP Addresses and Geo Locations.


```csharp
Task<Standard.Models.AllContentsResponse> AllContents()
```

#### Example Usage

```csharp

Standard.Models.AllContentsResponse result = await blacklist.AllContents();

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


[Back to List of Controllers](#list_of_controllers)

## <a name="users_login_registration_controller"></a>![Class: ](https://apidocs.io/img/class.png "BouncerAPI.Tests.Controllers.UsersLoginRegistrationController") UsersLoginRegistrationController

### Get singleton instance

The singleton instance of the ``` UsersLoginRegistrationController ``` class can be accessed from the API Client.

```csharp
UsersLoginRegistrationController usersLoginRegistration = client.UsersLoginRegistration;
```

### <a name="login_to_bouncer_api"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.UsersLoginRegistrationController.LoginToBouncerAPI") LoginToBouncerAPI

> Authenticate to this Bouncer instance.


```csharp
Task<Standard.Models.LoginToBouncerAPIResponse> LoginToBouncerAPI(Standard.Models.LoginToBouncerAPIRequest body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```csharp
var body = new Standard.Models.LoginToBouncerAPIRequest();

Standard.Models.LoginToBouncerAPIResponse result = await usersLoginRegistration.LoginToBouncerAPI(body);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="register_new_user"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.UsersLoginRegistrationController.RegisterNewUser") RegisterNewUser

> ONLY AVAILABLE when Bouncer is started with the `--testing` parameter.
> 
> Register a new user with this instance of Bouncer.


```csharp
Task<Standard.Models.RegisterNewUserResponse> RegisterNewUser(Standard.Models.RegisterNewUserRequest body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```csharp
var body = new Standard.Models.RegisterNewUserRequest();

Standard.Models.RegisterNewUserResponse result = await usersLoginRegistration.RegisterNewUser(body);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


[Back to List of Controllers](#list_of_controllers)

## <a name="whitelist_geo_locations_controller"></a>![Class: ](https://apidocs.io/img/class.png "BouncerAPI.Tests.Controllers.WhitelistGeoLocationsController") WhitelistGeoLocationsController

### Get singleton instance

The singleton instance of the ``` WhitelistGeoLocationsController ``` class can be accessed from the API Client.

```csharp
WhitelistGeoLocationsController whitelistGeoLocations = client.WhitelistGeoLocations;
```

### <a name="remove"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.WhitelistGeoLocationsController.Remove") Remove

> Remove a Geo Location in the Whitelist


```csharp
Task<Standard.Models.RemoveResponse1> Remove(string entryId, Standard.Models.GeoLocation body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```csharp
string entryId = "entry_id";
var body = new Standard.Models.GeoLocation();

Standard.Models.RemoveResponse1 result = await whitelistGeoLocations.Remove(entryId, body);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="update"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.WhitelistGeoLocationsController.Update") Update

> Update a Geo Location in the Whitelist


```csharp
Task<Standard.Models.UpdateResponse1> Update(string entryId, Standard.Models.GeoLocation body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```csharp
string entryId = "entry_id";
var body = new Standard.Models.GeoLocation();

Standard.Models.UpdateResponse1 result = await whitelistGeoLocations.Update(entryId, body);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="create"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.WhitelistGeoLocationsController.Create") Create

> Create a Geo Location in the Whitelist. When POSTed-to this endpoint, Bouncer scans `geolist.txt` for any IPs matching the Country Code (CC) in the POSTed object and, for each: Bouncer will create a new ipaddress in this list (black- or white-list).


```csharp
Task<Standard.Models.CreateResponse1> Create(Standard.Models.GeoLocation body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```csharp
var body = new Standard.Models.GeoLocation();

Standard.Models.CreateResponse1 result = await whitelistGeoLocations.Create(body);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="get_details"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.WhitelistGeoLocationsController.GetDetails") GetDetails

> Get Details of a Geo Location Entry in the Whitelist


```csharp
Task<Standard.Models.GetDetailsResponse1> GetDetails(string entryId)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |


#### Example Usage

```csharp
string entryId = "884d9804999fc47a3c2694e49ad2536a";

Standard.Models.GetDetailsResponse1 result = await whitelistGeoLocations.GetDetails(entryId);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="list"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.WhitelistGeoLocationsController.List") List

> List all Geo Locations in the Whitelist


```csharp
Task<Standard.Models.ListResponse1> List()
```

#### Example Usage

```csharp

Standard.Models.ListResponse1 result = await whitelistGeoLocations.List();

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


[Back to List of Controllers](#list_of_controllers)

## <a name="blacklist_geo_locations_controller"></a>![Class: ](https://apidocs.io/img/class.png "BouncerAPI.Tests.Controllers.BlacklistGeoLocationsController") BlacklistGeoLocationsController

### Get singleton instance

The singleton instance of the ``` BlacklistGeoLocationsController ``` class can be accessed from the API Client.

```csharp
BlacklistGeoLocationsController blacklistGeoLocations = client.BlacklistGeoLocations;
```

### <a name="remove"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.BlacklistGeoLocationsController.Remove") Remove

> Remove a Geo Location in the Blacklist


```csharp
Task<Standard.Models.RemoveResponse1> Remove(string entryId, Standard.Models.GeoLocation body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```csharp
string entryId = "entry_id";
var body = new Standard.Models.GeoLocation();

Standard.Models.RemoveResponse1 result = await blacklistGeoLocations.Remove(entryId, body);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="create"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.BlacklistGeoLocationsController.Create") Create

> Create a Geo Location in the Blacklist. When POSTed-to this endpoint, Bouncer scans `geolist.txt` for any IPs matching the Country Code (CC) in the POSTed object and, for each: Bouncer will create a new ipaddress in this list (black- or white-list).


```csharp
Task<Standard.Models.CreateResponse1> Create(Standard.Models.GeoLocation body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```csharp
var body = new Standard.Models.GeoLocation();

Standard.Models.CreateResponse1 result = await blacklistGeoLocations.Create(body);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="update"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.BlacklistGeoLocationsController.Update") Update

> Update a Geo Location in the Blacklist


```csharp
Task<Standard.Models.UpdateResponse1> Update(string entryId, Standard.Models.GeoLocation body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```csharp
string entryId = "entry_id";
var body = new Standard.Models.GeoLocation();

Standard.Models.UpdateResponse1 result = await blacklistGeoLocations.Update(entryId, body);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="list"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.BlacklistGeoLocationsController.List") List

> List all Geo Locations in the Blacklist


```csharp
Task<Standard.Models.ListResponse1> List()
```

#### Example Usage

```csharp

Standard.Models.ListResponse1 result = await blacklistGeoLocations.List();

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="get_details"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.BlacklistGeoLocationsController.GetDetails") GetDetails

> Get Details of a Geo Location Entry in the Blacklist


```csharp
Task<Standard.Models.GetDetailsResponse1> GetDetails(string entryId)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the Geo Location; opaque but likely a GUID |


#### Example Usage

```csharp
string entryId = "884d9804999fc47a3c2694e49ad2536a";

Standard.Models.GetDetailsResponse1 result = await blacklistGeoLocations.GetDetails(entryId);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


[Back to List of Controllers](#list_of_controllers)

## <a name="check_ip_addresses_controller"></a>![Class: ](https://apidocs.io/img/class.png "BouncerAPI.Tests.Controllers.CheckIPAddressesController") CheckIPAddressesController

### Get singleton instance

The singleton instance of the ``` CheckIPAddressesController ``` class can be accessed from the API Client.

```csharp
CheckIPAddressesController checkIPAddresses = client.CheckIPAddresses;
```

### <a name="test_for_list_membership"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.CheckIPAddressesController.TestForListMembership") TestForListMembership

> Check if an IP Address is Already White- or Black-Listed


```csharp
Task<Standard.Models.TestForListMembershipResponse> TestForListMembership(string ipAddress)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| ipAddress |  ``` Required ```  | the IP address to check |


#### Example Usage

```csharp
string ipAddress = "192.168.100.14";

Standard.Models.TestForListMembershipResponse result = await checkIPAddresses.TestForListMembership(ipAddress);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


[Back to List of Controllers](#list_of_controllers)

## <a name="blacklist_ip_addresses_controller"></a>![Class: ](https://apidocs.io/img/class.png "BouncerAPI.Tests.Controllers.BlacklistIPAddressesController") BlacklistIPAddressesController

### Get singleton instance

The singleton instance of the ``` BlacklistIPAddressesController ``` class can be accessed from the API Client.

```csharp
BlacklistIPAddressesController blacklistIPAddresses = client.BlacklistIPAddresses;
```

### <a name="update"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.BlacklistIPAddressesController.Update") Update

> Update an IP Address in the Blacklist


```csharp
Task<Standard.Models.UpdateResponse> Update(string entryId, Standard.Models.IPAddress body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```csharp
string entryId = "entry_id";
var body = new Standard.Models.IPAddress();

Standard.Models.UpdateResponse result = await blacklistIPAddresses.Update(entryId, body);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="remove"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.BlacklistIPAddressesController.Remove") Remove

> Remove an IP Address in the Blacklist


```csharp
Task<Standard.Models.RemoveResponse> Remove(string entryId, Standard.Models.IPAddress body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```csharp
string entryId = "entry_id";
var body = new Standard.Models.IPAddress();

Standard.Models.RemoveResponse result = await blacklistIPAddresses.Remove(entryId, body);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="get_details"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.BlacklistIPAddressesController.GetDetails") GetDetails

> Get Details of an IP Address Entry in the Blacklist


```csharp
Task<Standard.Models.GetDetailsResponse> GetDetails(string entryId)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |


#### Example Usage

```csharp
string entryId = "884d9804999fc47a3c2694e49ad2536a";

Standard.Models.GetDetailsResponse result = await blacklistIPAddresses.GetDetails(entryId);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="create"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.BlacklistIPAddressesController.Create") Create

> Create an IP Address in the Blacklist


```csharp
Task<Standard.Models.CreateResponse> Create(Standard.Models.IPAddress body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```csharp
var body = new Standard.Models.IPAddress();

Standard.Models.CreateResponse result = await blacklistIPAddresses.Create(body);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="search"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.BlacklistIPAddressesController.Search") Search

> Search for IP Addresses in the Blacklist


```csharp
Task<Standard.Models.SearchResponse> Search(string searchFilter)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| searchFilter |  ``` Required ```  | an comma-separated lsit of IP addresses in CIDR format (`192.168.100.14/24`) except with `/` replaced by `+` |


#### Example Usage

```csharp
string searchFilter = "192.168.100.0+24,192.168.101.0+24";

Standard.Models.SearchResponse result = await blacklistIPAddresses.Search(searchFilter);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="list"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.BlacklistIPAddressesController.List") List

> List all IP Addresses in the Blacklist


```csharp
Task<Standard.Models.ListResponse> List()
```

#### Example Usage

```csharp

Standard.Models.ListResponse result = await blacklistIPAddresses.List();

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


[Back to List of Controllers](#list_of_controllers)

## <a name="whitelist_ip_addresses_controller"></a>![Class: ](https://apidocs.io/img/class.png "BouncerAPI.Tests.Controllers.WhitelistIPAddressesController") WhitelistIPAddressesController

### Get singleton instance

The singleton instance of the ``` WhitelistIPAddressesController ``` class can be accessed from the API Client.

```csharp
WhitelistIPAddressesController whitelistIPAddresses = client.WhitelistIPAddresses;
```

### <a name="remove"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.WhitelistIPAddressesController.Remove") Remove

> Remove an IP Address in the Whitelist


```csharp
Task<Standard.Models.RemoveResponse> Remove(string entryId, Standard.Models.IPAddress body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```csharp
string entryId = "entry_id";
var body = new Standard.Models.IPAddress();

Standard.Models.RemoveResponse result = await whitelistIPAddresses.Remove(entryId, body);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="update"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.WhitelistIPAddressesController.Update") Update

> Update an IP Address in the Whitelist


```csharp
Task<Standard.Models.UpdateResponse> Update(string entryId, Standard.Models.IPAddress body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```csharp
string entryId = "entry_id";
var body = new Standard.Models.IPAddress();

Standard.Models.UpdateResponse result = await whitelistIPAddresses.Update(entryId, body);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="create"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.WhitelistIPAddressesController.Create") Create

> Create an IP Address in the Whitelist


```csharp
Task<Standard.Models.CreateResponse> Create(Standard.Models.IPAddress body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |


#### Example Usage

```csharp
var body = new Standard.Models.IPAddress();

Standard.Models.CreateResponse result = await whitelistIPAddresses.Create(body);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="get_details"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.WhitelistIPAddressesController.GetDetails") GetDetails

> Get Details of an IP Address Entry in the Whitelist


```csharp
Task<Standard.Models.GetDetailsResponse> GetDetails(string entryId)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entryId |  ``` Required ```  | a unique identifier for the IP Address; opaque but likely a GUID |


#### Example Usage

```csharp
string entryId = "884d9804999fc47a3c2694e49ad2536a";

Standard.Models.GetDetailsResponse result = await whitelistIPAddresses.GetDetails(entryId);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="list"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.WhitelistIPAddressesController.List") List

> List all IP Addresses in the Whitelist


```csharp
Task<Standard.Models.ListResponse> List()
```

#### Example Usage

```csharp

Standard.Models.ListResponse result = await whitelistIPAddresses.List();

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


### <a name="search"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.WhitelistIPAddressesController.Search") Search

> Search for IP Addresses in the Whitelist


```csharp
Task<Standard.Models.SearchResponse> Search(string searchFilter)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| searchFilter |  ``` Required ```  | an comma-separated lsit of IP addresses in CIDR format (`192.168.100.14/24`) except with `/` replaced by `+` |


#### Example Usage

```csharp
string searchFilter = "192.168.100.0+24,192.168.101.0+24";

Standard.Models.SearchResponse result = await whitelistIPAddresses.Search(searchFilter);

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


[Back to List of Controllers](#list_of_controllers)

## <a name="whitelist_controller"></a>![Class: ](https://apidocs.io/img/class.png "BouncerAPI.Tests.Controllers.WhitelistController") WhitelistController

### Get singleton instance

The singleton instance of the ``` WhitelistController ``` class can be accessed from the API Client.

```csharp
WhitelistController whitelist = client.Whitelist;
```

### <a name="all_contents"></a>![Method: ](https://apidocs.io/img/method.png "BouncerAPI.Tests.Controllers.WhitelistController.AllContents") AllContents

> This will list the entire contents of the Whitelist including both IP Addresses and Geo Locations.


```csharp
Task<Standard.Models.AllContentsResponse> AllContents()
```

#### Example Usage

```csharp

Standard.Models.AllContentsResponse result = await whitelist.AllContents();

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |


[Back to List of Controllers](#list_of_controllers)



