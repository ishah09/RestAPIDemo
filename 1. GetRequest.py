import requests

requestURL = "https://reqres.in/api/users?page=2"

response = requests.get(requestURL, verify=False)

print("Response Code:", response)
print("Response Status Code:", response.status_code)
print("Response Content:", response.content)
print("Response Header:", response.headers)
print("Response Time:", response.elapsed)

json_response = response.json()
print("Specific Parameter URL:", json_response['support']['url'])
