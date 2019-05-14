using System;
using System.IO;
using System.Text;
using BouncerAPI.Standard;
using BouncerAPI.Standard.Exceptions;
using BouncerAPI.Standard.Models;

namespace SampleBouncerApiClient
{
    class BouncerClient
    {
        static BouncerClient()
        {
            // update to bouncer REST API Host
            Configuration.DefaultHost = "localhost:8080";
        }

        /// <summary>
        /// Test User and Password to use
        /// </summary>
        private static string TEST_USER = "testcsharp";
        private static string TEST_USER_PASSWORD = "csharp#2019";

        static void Main(string[] args)
        {
            registerNewUser();
            var blacklist_response = addBlackList("192.168.1.1");
            Console.WriteLine("Current Entries =>");
            print(listBlackList());
            if (blacklist_response != null)
            {
                Console.WriteLine("Removing Entry");
                // Note removing the blacklist only marks the entry as removed, the appliance will purge the record when
                // the scheduling service is run 
                removeBlackList(blacklist_response, "192.168.1.1");
                print(listBlackList());
            }
        }

        /// <summary>
        /// Register a new User with the Bouncer REST API
        /// <para>NOTE: The REST API must be started with --testing parameter to support User Registration</para>
        /// </summary>
        public static void registerNewUser()
        {
            var client = new BouncerAPIClient();
            try
            {
                var register_request = new RegisterNewUserRequest
                {
                    Username = TEST_USER,
                    Password = TEST_USER_PASSWORD
                };
                var register_response = client.UsersLoginRegistration.RegisterNewUser(register_request);
                Console.WriteLine($"Use Registered Successfully :- {register_response.Message}");
            }
            catch (APIException exception)
            {
                printException("Register New User =>", exception);
            }
        }

        /// <summary>
        /// Returns a reference to the Bouncer API SDK Client
        /// <para>This method automatically authenticates with the Bouncer REST API</para>
        /// </summary>
        /// <returns></returns>
        public static BouncerAPIClient getBouncerApiSdkClient()
        {
            var client = new BouncerAPIClient();
            if (string.IsNullOrWhiteSpace(Configuration.ACCESS_TOKEN))
            {
                var login_request = new LoginToBouncerAPIRequest
                {
                    Username = TEST_USER,
                    Password = TEST_USER_PASSWORD,
                    GrantType = "password"
                };
                var login_response = client.UsersLoginRegistration.LoginToBouncerAPI(login_request);
                Configuration.ACCESS_TOKEN = login_response.AccessToken;
            }

            return client;
        }

        /// <summary>
        /// Adds a whitelist IP Address entry to the Bouncer Appliance
        /// </summary>
        /// <param name="newIpAddress">IP Address to Add</param>
        /// <returns>Created Response, Null otherwise</returns>
        public static CreateResponse addWhiteList(string newIpAddress)
        {
            var client = getBouncerApiSdkClient();
            var ipAddress = new IPAddress
            {
                Active = true,
                Comments = "Adding IP Address",
                StartDate = DateTime.Now.Date.ToString("d"),
                EndDate = DateTime.Now.Date.AddYears(1).ToString("d"),
                IPv4 = newIpAddress
            };
            try
            {
                var response = client.WhitelistIPAddresses.Create(ipAddress);
                Console.WriteLine($"Successfully Added entry {response.Result.EntryID}");
                return response;
            }
            catch (APIException exception)
            {
                printException("Add White List =>", exception);
                return null;
            }
        }

        /// <summary>
        /// Adds a blacklist IP Address entry to the Bouncer Appliance
        /// </summary>
        /// <param name="newIpAddress">IP Address to Add</param>
        /// <returns>Created Response, Null otherwise</returns>
        public static CreateResponse addBlackList(string newIpAddress)
        {
            var client = getBouncerApiSdkClient();
            var ipAddress = new IPAddress
            {
                Active = true,
                Comments = "Adding IP Address",
                StartDate = DateTime.Now.Date.ToString("d"),
                EndDate = DateTime.Now.Date.AddYears(1).ToString("d"),
                IPv4 = newIpAddress
            };
            try
            {
                var response = client.BlacklistIPAddresses.Create(ipAddress);
                Console.WriteLine($"Successfully Added entry {response.Result.EntryID}");
                return response;
            }
            catch (APIException exception)
            {
                printException("Add Blacklist =>", exception);
                return null;
            }
        }

        /// <summary>
        /// Removes a blacklist IP Address entry from the Bouncer Appliance
        /// </summary>
        /// <param name="createResponse">Create Response (required to grab the entry id for deletion)</param>
        /// <param name="newIpAddress">IP Address to Remove</param>
        /// <returns>Remove Response, Null otherwise</returns>
        public static RemoveResponse removeBlackList(CreateResponse createResponse, string newIpAddress)
        {
            var client = getBouncerApiSdkClient();
            var ipAddress = new IPAddress
            {
                Active = true,
                Comments = "Removing IP Address",
                StartDate = DateTime.Now.Date.ToString("d"),
                EndDate = DateTime.Now.Date.AddYears(1).ToString("d"),
                IPv4 = newIpAddress
            };
            try
            {
                var remove_response = client.BlacklistIPAddresses.Remove(createResponse.Result.EntryID, ipAddress);
                Console.WriteLine($"Successfully Removed entry {remove_response.Result.EntryID}");
                return remove_response;
            }
            catch (APIException exception)
            {
                printException("Remove Blacklist =>", exception);
                return null;
            }
        }

        /// <summary>
        /// Lists the blacklist IP Address entry from the Bouncer Appliance
        /// </summary>
        /// <returns>Created Response, Null otherwise</returns>
        public static ListResponse listBlackList()
        {
            var client = getBouncerApiSdkClient();
            try
            {
                var list_response = client.BlacklistIPAddresses.List();
                return list_response;
            }
            catch (APIException exception)
            {
                printException("List Blacklist entries =>", exception);
                return null;
            }
        }

        /// <summary>
        /// Helper Method to print List Entries
        /// </summary>
        /// <param name="list"></param>
        private static void print(ListResponse list)
        {
            if (list == null)
            {
                Console.WriteLine("Empty list");
                return;
            }

            list.IPAddresses.ForEach(c => Console.WriteLine($"{c[0]}, {c[1]}"));
        }

        /// <summary>
        /// Helper Method to Print Exception
        /// </summary>
        /// <param name="forMethod">Method the Exception was raised</param>
        /// <param name="exception"></param>
        private static void printException(string forMethod, APIException exception)
        {
            if (exception.HttpContext.Response.RawBody is MemoryStream memoryStream)
            {
                var body = Encoding.UTF8.GetString(memoryStream.ToArray());
                Console.WriteLine($"{forMethod} - {body}");
            }
            else
            {
                Console.WriteLine(exception);
            }
        }
    }
}
