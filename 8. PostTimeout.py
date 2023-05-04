import requests

url = "https://reqres.in/api/users"
payload = {
    "name": "Ishita",
    "job": "Shah"
}

response = requests.post(url, data=payload, timeout=1, verify=False)

print("Response Code:", response)
print("Response Status Code:", response.status_code)

response = requests.post(url, data=payload, timeout=0.1, verify=False)

print("Response Code:", response)
print("New Response Status Code:", response.status_code)
