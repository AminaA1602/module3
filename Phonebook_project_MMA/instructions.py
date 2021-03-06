# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 14:07:01 2019

@author: Skitt
"""

#1.1.1 Find businesses by business type in the vicinity of a specified postcode.
#  Step 1: User inputs the business type and the postcode.
#    -Function name: getBusinessTypeAndPostcode.
#    -Inputs and outputs:
#                        No inputs
#                        Returns business type and postcode
#  Step 2: Retrieve longitude and latitude using the postcode provided by the user.
#    -Function name: getLongitudeAndLatitudeForInputPostcode
#    -Inputs and outputs:
#                       - One input: input postcode from getBusinessTypeAndPostcode
#                       - Returns longitude and latitude for the input postcode
#  Step 3: Retrieve all the postcodes for all the businesses in my table with that business type.
#    -Function name: getAllPostcodesForInputBusinessType
#    - Inputs and outputs:
#                        - Two inputs: business type and connection to database
#                        - Returns a list of postcodes
#  Step 4: Retrieve the longitude and latitudes for the postcodes from step 3.
#    -Function name: getLongitudeAndLatitudeForAllPostcodes
#    - Inputs and outputs:
#                      - Two inputs: list of postcodes from getAllPostcodesForInputBusinessType and connection to database.
#                      - Return a dictionary where the postcode is a key and longitude and latitude are the values.
#  Step 5: Calculate the relative distance from input postcode and the business postcode.
#    -Function name: calculateRelativeDistanceBetweenInputPostcodeAndAllPostcode
#    - Inputs and outputs:
#                        -Two inputs: return from getLongitudeAndLatitudeForInputPostcode and return from getLongitudeAndLatitudeForAllPostcodes
#                        -Returns a dictionary where the key is the postcode and the value is the distance calculated.
#  Step 6: Sort the postcodes, nearest to furthest in relation to input postcode.
#    -Function name: sortPostcodeBasedOnDistances
#    -Inputs and Outputs:
#                        - One input: The return from the function calculate RelativeDistanceBetweenInputPostcodeAndAllPostcode
#                        - Returns a sorted dictionary based on distance.
#  Step 7: Retrieve the business name, phone number and relative distance for a maximum of 50 postcodes from step 6.
#    -Function name: getBusinessNamePhoneNumberAndDistanceForPostcodes
#    -Inputs and outputs:
#                        - Two inputs: The return from sortPostcodeBasedOnDistances and the connection to the database.
#                        - Returns a list of dictionaries, each dictionary will have one key value pair, the key being the postcode and the value is
#                          a list containing the distance, name and phone number.
#    -Function name: getVariablesStoringBusinessNamePhoneNumberAndDistanceForPostcodes
#    -Inputs and outputs:
#                        - One input: The return from getBusinessNamePhoneNumberAndDistanceForPostcodes
#                          - Returns ?????????
#1.1.2 Find businesses by business name in the vicinity of a specified postcode.
#  Step 1: User inputs the business name and the postcode.
#  Step 2: Retrieve longitude and latitude using the postcode provided by the user.
#  Step 3: Retrieve all the postcodes for all the businesses in my table with that business name.
#  Step 4: Retrieve the longitude and latitudes for the postcodes from step 3.
#  Step 5: Calculate the relative distance from input postcode and the business postcode.
#  Step 6: Sort the postcodes, nearest to furthest in relation to input postcode.
#  Step 7: Retrieve and display the business name and phone number and relative distance for a maximum of 50 postcodes from step 6.