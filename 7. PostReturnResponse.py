import requests

url = "https://reqres.in/api/register"
payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

response = requests.post(url, data=payload, verify=False)
print(response.json()['token'])