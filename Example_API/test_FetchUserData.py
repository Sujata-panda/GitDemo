import requests
# https://reqrs.in
# base url-https://reqres.in/
# relative url/URI-/api/users?page=2
#  so URL= https://reqres.in/api/users?page=2

class TestDemo:
  url = "https://reqres.in/api/users?page=2"
  def test_getdemo(self):
       response = requests.get(object.url)
       print(response)
       print(response.content)
object=TestDemo()
print(object.test_getdemo())


