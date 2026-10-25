import subprocess
import pickle
import os

API_KEY = "sk-1234567890abcdef"
password = "supersecret123"

def run_command(user_input):
    os.system("ls " + user_input)
    subprocess.call(user_input, shell=True)

def load_data(data):
    return pickle.loads(data)

def get_user(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return query
