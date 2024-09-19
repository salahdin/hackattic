import requests
import hashlib
import hmac
import base64
from challenge_soln_urls import challenges


CHALLENGE_API_ROUTE, SOLUTION_URL = challenges['password_hashing']
ch = requests.get(CHALLENGE_API_ROUTE).json()


def calculate_sha256(password: str, _salt: str) -> str:
    salted_password = password.encode() + _salt
    hash_obj = hashlib.sha256(salted_password)
    return hash_obj.hexdigest()


def calculate_hmac(password: str, key: str) -> str:
    hm = hmac.new(key.encode(), password.encode(), hashlib.sha256)
    return hm.hexdigest()


