1) Update Bouncer Rest API DNS Host
2) Update User Name and Password in BouncerClient.py
   NOTE: Bouncer supports new registration only if the Bouncer Rest API was started in testing mode
3) update BouncerAPI.Standanrd.Configuration and add a static string field called ACCESS_TOKEN and set its value to null. The Value for this field
is set in the getBouncerApiSdkClient() method in BouncerClient.cs
4) Update BouncerAPI.Standard.AuthUtility and add ACCESS_TOKEN to Authorization Header as "Bearer {ACCESS_TOKEN}"
		if (!string.IsNullOrWhiteSpace(Configuration.ACCESS_TOKEN))
		{
			request.Headers.Add("Authorization", $"Bearer {Configuration.ACCESS_TOKEN}");
		}
5) Execute Application => dotnet SampleBouncerApiClient