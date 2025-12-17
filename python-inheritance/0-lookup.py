def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    
    Args:
        obj: Any Python object
        
    Returns:
        list: A list of strings representing the attributes and methods
    """
    return dir(obj)
