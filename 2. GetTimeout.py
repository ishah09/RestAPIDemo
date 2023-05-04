import requests

requestURL = "https://reqres.in/api/users?page=2"

response = requests.get(requestURL, timeout=1, verify=False)

print("Response Code:", response)
print("Response Status Code:", response.status_code)

response = requests.get(requestURL, timeout=0.1, verify=False)

print("Response Code:", response)
print("New Response Status Code:", response.status_code)
