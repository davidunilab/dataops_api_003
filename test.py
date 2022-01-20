import requests
BASE_URL = "http://localhost:5000/"
data = [
    {"name": 'Flask Tutorial', "views": 120, "likes": 432, },
    {"name": 'C++ Tutorial', "views": 1825, "likes": 185, },
    {"name": 'Java Tutorial', "views": 1234, "likes": 894, },
]


for i in range(len(data)):
    response = requests.put(BASE_URL + 'video/%d'%i, data[i])
    print(response.json())

# response = requests.get(BASE_URL + 'helloworld/davit/32')
# print(response.json())
input('Enter to next test\n')
response = requests.delete(BASE_URL + 'video/0')
print(response)


input('Enter to next test\n')
response = requests.get(BASE_URL + 'video/2')
print(response.json())

