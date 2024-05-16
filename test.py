import requests
from json import loads

url = 'http://localhost:8000/api/v1/idcard/'

files = {'photo': open('pic/img_2.png', 'rb')}

response = requests.post(url, files=files)

print(loads(response.content))

# Remember to close the file after using it
files['photo'].close()
