import requests

url = "https://reqres.in/api/users/2"

payload = {
    "name": "Ishita",
    "job": "zion resident"
}

response = requests.put(url, data=payload, verify=False)
print(response.json())