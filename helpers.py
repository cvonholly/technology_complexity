
special_keys = {
    'api/v1/ipc'                      : 'ipcr',
    'api/v1/wipo'                     : 'wipo',
}

def response_key(endpoint:str) -> str:
    """
    Given the API endpoint contacted, returns the json key for the data returned by the API.
    In most cases, this is the plural of the term at the end of the endpoint URL.
    """
    endpoint = endpoint.rstrip('/')
    leaf = endpoint.split('/')[-1]
    if leaf in special_keys:
        return special_keys[leaf]
    elif leaf.endswith('s'):
        return leaf + 'es'
    else:
        return leaf + 's'