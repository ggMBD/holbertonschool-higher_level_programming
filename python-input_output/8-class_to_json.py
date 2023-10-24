def class_to_json(obj):
    """
    function that returns the dictionary
    description with simple data structure
    for JSON serialization.
    """
    if not isinstance(obj, object):
        raise TypeError("input must be a class")

    attributes = {}
    for attr_key, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            attributes[attr_key] = attr_value

    return attributes
