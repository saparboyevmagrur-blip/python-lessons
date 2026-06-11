# API - Application Programming Interface
# request(so'rov) # response(javob)
# JSON (JavaScript Object Notation)
# HTTP / HTTPS request methods:
# 1. GET(data olish) 
# 2. POST(data yuborish)
# 3. PUT/PATCH(bor datani yangilash)
# 4. DELETE(datani o'chirib)
import requests

# Make a request
response = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(response.status_code)
# Get data as JSON
data = response.json()
print(data)
