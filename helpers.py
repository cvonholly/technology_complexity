
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
    


# for claims
import pandas as pd
import re
import math as mt

def get_claims(df: pd.DataFrame, id: int) -> pd.DataFrame:
    claims_text = df.loc[(df['Publn_Nr'] == id) & (df['Type'].str.match('Claim')), 'Text']  # get claim text
    return claims_text

def concantenate_claims(claims: pd.Series) -> str:
    return ' '.join(claims)

def checkRoman(token):
    re_pattern = '[mdcxvi]+[a-z]'
    if re.fullmatch(re_pattern, token):
        return True
    return False

def update_total_counts(counts_total: dict, tokens: list) -> dict:
    for token, count in tokens.items():
        if token in counts_total:
            counts_total[token] += count
        else:
            counts_total[token] = count
    return counts_total

def get_entropy(counts: dict) -> float:
    """
    Calculate the entropy of a dictionary of token counts
    """
    entropy = 0
    total = sum(counts.values())
    for token, count in counts.items():
        if count > 0:
            p = count / total
            entropy = p * mt.log2(1/p)
    return entropy