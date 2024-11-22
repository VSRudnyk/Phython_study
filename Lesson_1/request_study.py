import requests

site = 'https://jsonplaceholder.typicode.com/posts/1'

responce_get = requests.get(url=site)

# for header, value in responce_get.headers.items():
#     print(f'{header}: {value}')


print(responce_get.text)
# print ('------------')

# body = {
#     'userId': 12,
#     'title': 'test',
#     'body': 'test'
# }

# headers = {
#     'Content-Type': 'application/json; charset=utf-8'
# }

# responce_post = requests.post(url=site, json=body, headers=headers)
# print(responce_post.status_code)
# print(responce_post.reason)
# print(responce_post.text)
# print ('------------')

data= {
    'title': 'test_put'
}

response_put = requests.put(url=site, data=data)
print(response_put.status_code)
print(response_put.reason)
print(response_put.text)

response_patch = requests.patch(url=site, data=data)
print(response_patch.status_code)
print(response_patch.reason)
print(response_patch.text)

response_delete = requests.delete(url=site, data=data)
print(response_delete.status_code)
print(response_delete.reason)
print(response_delete.text)