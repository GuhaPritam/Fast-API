import requests

url = 'http://192.168.1.87:8000/users'
data1 = {
    "_id": "2",
    "name": "chiku",
    "email": "chi@3"
}

put_response = requests.put("http://192.168.1.87:8000/users", json=data1)

post_response = requests.post(url, json=data1)

