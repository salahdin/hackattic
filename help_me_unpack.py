import requests
import base64
import struct

from challenge_soln_urls import challenges

CHALLENGE_API_ROUTE, SOLUTION_URL = challenges['help_me_unpack']


def get_initial_data():
    response = requests.get(CHALLENGE_API_ROUTE)
    return response.json()


def generate_response(data):
    # convert base64 string to bytes
    base64_decoded = base64.b64decode(data['bytes'])
    ret_val = dict(
        int=int.from_bytes(base64_decoded[:4], byteorder='little', signed=True),
        uint=int.from_bytes(base64_decoded[4:8], byteorder='little', signed=False),
        short=struct.unpack('<h', base64_decoded[8:10])[0],
        float=struct.unpack('<f', base64_decoded[12:16])[0],
        double=struct.unpack('<d', base64_decoded[16:24])[0],
        big_endian_double=struct.unpack('>d', base64_decoded[24:32])[0],
    )
    return ret_val


if __name__ == '__main__':
    initial_data = get_initial_data()

    res = requests.post(
        SOLUTION_URL,
        json=generate_response(initial_data)
    )
    print(res.json())
