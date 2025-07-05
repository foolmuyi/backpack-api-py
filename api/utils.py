import base64
import time
import nacl.signing
from . import consts as c


def clean_dict_none(d):
    return {k:d[k] for k in d.keys() if d[k] != None}

def convert_bool(obj):
   if isinstance(obj, bool):
       return "true" if obj else "false"
   elif isinstance(obj, dict):
       return {k: convert_bool(v) for k, v in obj.items()}
   elif isinstance(obj, list):
       return [convert_bool(item) for item in obj]
   return obj

def sign(message, secret_key):
    secret_key_bytes = base64.b64decode(secret_key)
    signing_key = nacl.signing.SigningKey(secret_key_bytes)
    signed = signing_key.sign(message.encode())
    signature = base64.b64encode(signed.signature).decode()
    return signature


def pre_hash(instruction, params, timestamp, window):
    str_to_sign = 'instruction=' + str(instruction)
    params = convert_bool(clean_dict_none(params))
    sorted_params = sorted(params.items())
    for each in sorted_params:
        str_to_sign += ('&' + str(each[0]) + '=' + str(each[1]))
    str_to_sign += ('&timestamp=' + str(timestamp) + '&window=' + str(window))
    return str_to_sign


def get_header(api_key, sign, timestamp, window):
    header = dict()
    header[c.X_API_KEY] = api_key
    header[c.X_SIGNATURE] = sign
    header[c.X_TIMESTAMP] = str(timestamp)
    header[c.X_WINDOW] = window
    return header


def parse_params_to_str(params):
    params = convert_bool(clean_dict_none(params))
    sorted_params = sorted(params.items())
    url = '?'
    for each in sorted_params:
        url = url + str(each[0]) + '=' + str(each[1]) + '&'
    return url[0:-1]


def get_timestamp():
    return int(time.time()*1000)