# -*- coding: utf-8 -*-

"""
    bouncerapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import bouncerapi.models.result_9

class CreateResponse1(object):

    """Implementation of the 'Create response1' model.

    TODO: type model description here.

    Attributes:
        result (Result9): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "result":'Result'
    }

    def __init__(self,
                 result=None):
        """Constructor for the CreateResponse1 class"""

        # Initialize members of the class
        self.result = result


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
        result = bouncerapi.models.result_9.Result9.from_dictionary(dictionary.get('Result')) if dictionary.get('Result') else None

        # Return an object of this model
        return cls(result)

