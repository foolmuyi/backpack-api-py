import json
import httpx
from . import utils
from . import consts as c


class Client(object):

    def __init__(self, api_key=None, api_secret=None, proxy=None):

        self.API_KEY = api_key
        self.API_SECRET = api_secret
        self.window = c.DEFAULT_WINDOW
        self.client = httpx.Client(http2=True, proxy=proxy)

    def _request(self, instruction, method, request_path, params):

        if method == c.GET:
            request_path = request_path + utils.parse_params_to_str(params)
        url = c.API_URL + request_path

        timestamp = utils.get_timestamp()  # local time
        # timestamp = self._get_timestamp()  # server time

        body = "" if method == c.GET else json.dumps(params, sort_keys=True)

        if instruction == None:
            header = {}
        else:
            sign = utils.sign(utils.pre_hash(instruction, params, timestamp, self.window), self.API_SECRET)
            header = utils.get_header(self.API_KEY, sign, timestamp, self.window)

        # send request
        response = None

        # print("url:", url)
        # print("headers:", header)
        # print("body:", body)

        if method == c.GET:
            response = self.client.get(url, headers=header)
        elif method == c.POST:
            response = self.client.post(url, data=body, headers=header)

        # exception handle
        # print(response.headers)

        if not str(response.status_code).startswith('2'):
            print(response.reason)
            pass
            # raise exceptions.OkexAPIException(response)

        if request_path == c.PING.path:
            return response.text
        else:
            return response.json()

    def _request_without_params(self, instruction, method, request_path):
        return self._request(instruction, method, request_path, {})

    def _request_with_params(self, instruction, method, request_path, params):
        return self._request(instruction, method, request_path, params)

    def _get_timestamp(self):
        url = c.API_URL + c.SYSTEM_TIME
        response = self.client.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return ""
