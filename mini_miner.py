import requests
import json
import hashlib
from challenge_soln_urls import challenges

CHALLENGE_API_ROUTE, SOLUTION_URL = challenges['mini_miner']


def get_initial_data():
    response = requests.get(CHALLENGE_API_ROUTE)
    response.raise_for_status()  # Ensure the request was successful
    return response.json()


def calculate_sha256(byte_string):
    sha256_hash = hashlib.sha256(byte_string.encode())
    return sha256_hash.hexdigest()


def serialize_block(json_val):
    # Serialize JSON object without whitespace and with sorted keys
    return json.dumps(json_val, sort_keys=True, separators=(',', ':'))


def meets_difficulty(hash_hex, difficulty):
    # Convert hex hash to binary string
    hash_binary = bin(int(hash_hex, 16))[2:].zfill(256)  # Ensure 256 bits length
    # Check if it starts with the required number of zero bits
    return hash_binary.startswith('0' * difficulty)


if __name__ == '__main__':
    initial_data = get_initial_data()
    difficulty = initial_data['difficulty']
    block = initial_data['block']
    block['nonce'] = 0

    while True:
        # Serialize block with current nonce
        serialized_block = serialize_block(block)
        # Calculate SHA256 hash of the serialized block
        sha256_hashed = calculate_sha256(serialized_block)
        # Check if the hash meets the difficulty requirement
        if meets_difficulty(sha256_hashed, difficulty):
            break
        # Increment nonce and try again
        block['nonce'] += 1

    req = dict(nonce=block['nonce'])
    res = requests.post(
        "https://hackattic.com/challenges/mini_miner/solve?access_token=b476cf69f3e0d352",
        json.dumps(req)
    )
    print(res.json())
