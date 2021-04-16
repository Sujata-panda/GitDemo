import requests


# API
def test_getdemo():
    url = "https://reqres.in/api/users?page=2"

# send get request
    response = requests.get(url)
    print(response)

# display response content
    print(response.content)

test_getdemo()


