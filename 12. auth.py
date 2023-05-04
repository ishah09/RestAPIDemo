import requests

url = "https://the-internet.herokuapp.com/basic_auth"

response = requests.get(url, auth=("admin", "demo"), verify=False)
print("Response:", response)
