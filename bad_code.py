# bad_code.py
import pickle
password = "supersecret123"
api_key = "sk-abcdefghijklmnop1234567890"

def process(data):
    return eval(data)

def load(f):
    return pickle.load(f)
