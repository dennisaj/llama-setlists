
from uplink import Consumer, QueryMap, get, params, json, headers, returns, hooks, auth, clients
from typing import Optional
import os
import aiohttp

@params({"itemsPerPage": "100"})
@headers({'Accept': 'application/json'})
@get
def get_json(): """Template for GET request that consumes and produces JSON."""

class SetListApp(Consumer):
    def __init__(self, setlist_token: Optional[str] = None):
        if setlist_token is None:
            setlist_token = os.environ["SETLIST_TOKEN"]
        if setlist_token is None:
            raise ValueError("Must specify `setlist_token` or set environment variable `SETLIST_TOKEN`.")
        token_auth = auth.ApiTokenHeader("x-api-key", setlist_token)
        
        t = aiohttp.TCPConnector(verify_ssl=False)
        s = aiohttp.ClientSession(skip_auto_headers=['Content-Length'], trust_env=True, connector=t)
        client = clients.AiohttpClient(session = s)
        super(SetListApp, self).__init__(auth=token_auth, client=client, base_url="https://api.setlist.fm")

    @get_json("/rest/1.0/search/setlists")
    async def get_setList(self, **params: QueryMap):
        pass

