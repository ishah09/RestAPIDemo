import requests

url = "https://reqres.in/api/users"
payload = {
    "name": "Ishita",
    "job": "Shah"
}

response = requests.post(url, data=payload, verify=False)
print(response.json())

assert response.json()["job"] == 'Shah'

