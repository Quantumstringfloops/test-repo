import subprocess
import pickle
import os

# hardcoded secret
API_KEY = "sk-1234567890abcdef"
password = "supersecret123"

# command injection risk
def run_command(user_input):
    os.system("ls " + user_input)  # dangerous
    subprocess.call(user_input, shell=True)  # also dangerous

# insecure deserialization
def load_data(data):
    return pickle.loads(data)  # unsafe

# sql injection risk
def get_user(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return query