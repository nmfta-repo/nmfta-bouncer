using System.Collections.Generic;
using System.Text;
using BouncerAPI.Standard.Utilities;
using BouncerAPI.Standard.Models;
namespace BouncerAPI.Standard
{
    public partial class Configuration
    {


        public enum Environments
        {
            PRODUCTION,
        }
        public enum Servers
        {
            ENUM_DEFAULT,
        }

        //The current environment being used
        public static Environments Environment = Environments.PRODUCTION;

        //TODO: Replace the DefaultHost with an appropriate value
        public static string DefaultHost = "www.example.com";

        public static string ACCESS_TOKEN = null;

        //A map of environments and their corresponding servers/baseurls
        public static Dictionary<Environments, Dictionary<Servers, string>> EnvironmentsMap =
            new Dictionary<Environments, Dictionary<Servers, string>>
            {
                { 
                    Environments.PRODUCTION,new Dictionary<Servers, string>
                    {
                        { Servers.ENUM_DEFAULT,"http://{defaultHost}" },
                    }
                },
            };

        /// <summary>
        /// Makes a list of the BaseURL parameters 
        /// </summary>
        /// <return>Returns the parameters list</return>
        internal static List<KeyValuePair<string, object>> GetBaseURIParameters()
        {
            List<KeyValuePair<string, object>> kvpList = new List<KeyValuePair<string, object>>()
            {
                new KeyValuePair<string, object>("defaultHost", DefaultHost),
            };
            return kvpList; 
        }

        /// <summary>
        /// Gets the URL for a particular alias in the current environment and appends it with template parameters
        /// </summary>
        /// <param name="alias">Default value:DEFAULT</param>
        /// <return>Returns the baseurl</return>
        internal static string GetBaseURI(Servers alias = Servers.ENUM_DEFAULT)
        {
            StringBuilder Url =  new StringBuilder(EnvironmentsMap[Environment][alias]);
            APIHelper.AppendUrlWithTemplateParameters(Url, GetBaseURIParameters());
            return Url.ToString();        
        }
    }
}