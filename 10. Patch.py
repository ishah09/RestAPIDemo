import requests

url = "https://reqres.in/api/users/2"

payload = {
    "name": "Ishita Shah",
    "job": "zion resident"
}

response = requests.patch(url, data=payload, verify=False)
print(response.json())