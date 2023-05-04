import requests

url = "https://reqres.in/api/users/2"

response = requests.delete(url, verify=False)
print(response.json())
print("Status Code:" ,response.status_code)

assert response.status_code == 204, "User Deletion Success"
