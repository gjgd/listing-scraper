import requests
from requests.adapters import HTTPAdapter, Retry
from tqdm import tqdm
import math
import itertools

class EnhancedSession(requests.Session):
    '''
    Set timeout at the session level .
    '''
    def __init__(self, timeout=(3.05, 4)):
        self.timeout = timeout
        return super().__init__()

    def request(self, method, url, **kwargs):
        # print("EnhancedSession request")
        if "timeout" not in kwargs:
            kwargs["timeout"] = self.timeout
        return super().request(method, url, **kwargs)

def prepare_session():
    '''
    Prepare requests session with default timeout and retry.
    '''
    s = EnhancedSession(timeout=10)
    retries = Retry(total=5,
                    backoff_factor=0.1,
                    method_whitelist=["POST", "GET"])
    s.mount('http://', HTTPAdapter(max_retries=retries))
    s.mount('https://', HTTPAdapter(max_retries=retries))
    return s

def get_listings(eventid, quantity=None):
    '''
    Get all event listings.
    '''
    s = prepare_session()

    if type(eventid) is list:
        res = []
        for e in eventid:
            res.append(get_listings(e, quantity))
        return res

    url = f"https://www.stubhub.com/event/{eventid}"
    if quantity is not None:
        url += f"?quantity={quantity}"
    url = s.request("POST", url,allow_redirects=True).url
    data ={"PageSize": 100}
    response = s.request("POST", url, data=data)
    if response.status_code == 404:
        print('404, Probably, no listings for event {}'.format(eventid))
        return None

    respjson= response.json()
    querystring = {"CurrentPage":"1"}
    total_pages = math.ceil((respjson['TotalCount'] - 2*respjson['PageSize'])/respjson['PageSize'])
    items = respjson['Items']
    item_dicts = []
    with tqdm(total=total_pages, desc=f'Event Id: {eventid}', leave=False) as pbar:
        while respjson['ItemsRemaining'] > 0:
            item_dicts.append(items)

            querystring['CurrentPage'] = int(querystring['CurrentPage']) + 1
            respjson = s.request("POST", url, params=querystring, data=data).json()
            items = respjson['Items']
            pbar.set_description(f'Code: {response.status_code} Event Id: {eventid}')
            pbar.update(1)

        # append last page
        item_dicts.append(items)

    return list(itertools.chain.from_iterable(item_dicts))

def parse_listing(l):
    '''
    Parse listing by extracting relevant columns.
    '''
    listing = {}
    columns = {}
    for c in columns:
        listing[columns[c]] = l[c]

    return listing
