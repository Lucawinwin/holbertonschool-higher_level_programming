#!/usr/bin/python3
def class_to_json(obj):
    # Create an empty dictionary to hold serializable attributes
    json_dict = {}
    
    # Loop through the object's attributes using __dict__ to get its instance variables
    for attr, value in obj.__dict__.items():
        # Check if the attribute value is of a serializable type
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    
    return json_dict

