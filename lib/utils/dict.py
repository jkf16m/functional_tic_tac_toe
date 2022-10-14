def extract_and_map(dict, keys, function):
    """Extracts values from a dictionary and applies a function to each value.
    The function should return a tuple of two values, the first one is the key
    for the new dictionary and the second one is the value.
    """
    result = {}
    for key in keys:
        if key in dict:
            new_key, new_value = function(dict[key])
            result[new_key] = new_value
    return result