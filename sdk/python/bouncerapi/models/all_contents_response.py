# -*- coding: utf-8 -*-

"""
    bouncerapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import bouncerapi.models.result

class AllContentsResponse(object):

    """Implementation of the 'All Contents response' model.

    TODO: type model description here.

    Attributes:
        result (Result): TODO: type description here.
        ip_addresses (list of string): matching IP Address Objects found
        geo_locations (list of string): matching Geo Location Objects (in
            short string form `{id}#{cc}`) found

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "result":'Result',
        "ip_addresses":'IPAddresses',
        "geo_locations":'GeoLocations'
    }

    def __init__(self,
                 result=None,
                 ip_addresses=None,
                 geo_locations=None):
        """Constructor for the AllContentsResponse class"""

        # Initialize members of the class
        self.result = result
        self.ip_addresses = ip_addresses
        self.geo_locations = geo_locations


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        result = bouncerapi.models.result.Result.from_dictionary(dictionary.get('Result')) if dictionary.get('Result') else None
        ip_addresses = dictionary.get('IPAddresses')
        geo_locations = dictionary.get('GeoLocations')

        # Return an object of this model
        return cls(result,
                   ip_addresses,
                   geo_locations)


