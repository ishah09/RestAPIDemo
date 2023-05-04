import json

import requests

requestURL = "https://reqres.in/api/users?page=2"

response = requests.get(requestURL, verify=False)
json_response = response.json()

print("Total:", json_response['total'])

assert json_response['total_pages'] == 2, "Total Pages should be 2"


print(json_response["data"][0]["email"])
assert (json_response["data"][0]["email"]).endswith("reqres.in"), "Email should ends with reqres.in"




