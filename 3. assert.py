import requests

requestURL = "https://reqres.in/api/users?page=2"

response = requests.get(requestURL, verify=False)

code = response.status_code=200

assert code == 200, "Code doesn't match"
assert code == 400, "Code doesn't match"

