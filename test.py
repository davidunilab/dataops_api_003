import requests
import random
BASE_URL = "http://localhost:5000/"
data = [
    {"name": 'Flask Tutorial', "views": random.randint(30,500), "likes": random.randint(30,500), },
    {"name": 'C++ Tutorial', "views": random.randint(30,500), "likes": random.randint(30,500), },
    {"name": 'Java Tutorial', "views": random.randint(30,500), "likes": random.randint(30,500), },
    {"name": 'Assembly Tutorial', "views": random.randint(30,500), "likes": random.randint(30,500), },
    {"name": 'C Tutorial', "views": random.randint(30,500), "likes": random.randint(30,500), },
]


for i in range(len(data)):
    response = requests.put(BASE_URL + 'video/%d'%i, data[i])
    print(response.json())


input('Enter to next test\n')
response = requests.get(BASE_URL + 'video/2')
print(response.json())

input('Enter to next test\n')
response = requests.delete(BASE_URL + 'video/0')
print(response)