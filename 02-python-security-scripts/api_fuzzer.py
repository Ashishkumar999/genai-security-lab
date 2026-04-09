import requests

url = "https://example.com/api/user/"

for i in range(1, 50):
    response = requests.get(url + str(i))
    print(i, response.status_code)
