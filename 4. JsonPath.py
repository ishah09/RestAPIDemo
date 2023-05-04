import json
import requests

requestURL = "https://reqres.in/api/users?page=2"
response = requests.get(requestURL, verify=False)

print("Text:", response.text)
print("Content:", response.content)
print("JSON:", response.json())

json_request = json.loads(response.content)
print("JSON Load:", json_request)


