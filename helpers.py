
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
    


# display the API's uber-helful X-Status-Reason in the unlikely event 
# that we make a bad request
def handle_request_error(response):
    if response.status_code == 400:
        x_header_value = response.headers.get("X-Status-Reason")
        if x_header_value:
            print(f"Error: {x_header_value}")
        else:
            print("400 Bad Request: No X-Status-Reason found")
        exit(1)
    else:
        response.raise_for_status()